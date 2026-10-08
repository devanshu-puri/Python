#!/usr/bin/env python3
"""Reads journey.json -> regenerates assets/dashboard.svg and README marker blocks."""
import hashlib, json, re
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
data = json.loads((ROOT / "journey.json").read_text(encoding="utf-8"))
WEIGHT = {"done": 1.0, "wip": 0.5, "todo": 0.0}
ICON = {"done": "✅", "wip": "🟡", "todo": "⬜"}
COLORS = ["#22c55e", "#14b8a6", "#06b6d4", "#3b82f6", "#6366f1",
          "#8b5cf6", "#d946ef", "#f43f5e", "#f97316", "#eab308"]


def topics(track):
    return [t for c in track["chapters"] for t in c["topics"]]


def pct(items):
    return round(100 * sum(WEIGHT[t["status"]] for t in items) / len(items)) if items else 0


def cell(s):
    return str(s).replace("|", "\\|").replace("\n", " ")


tracks = data["tracks"]

# ---------- auto-discovery of lesson files ----------
import ast
SKIP_DIRS = {".git", ".github", "assets", "scripts", "__pycache__", "venv", ".venv", "node_modules"}
EXTS = {".py", ".md", ".ipynb"}
IGNORE = set(data.get("ignore", ["README.md", "practice.py"]))


def rel_files(base):
    for p in sorted(base.rglob("*")):
        r = p.relative_to(ROOT)
        if p.is_file() and p.suffix in EXTS and not (set(r.parts[:-1]) & SKIP_DIRS) and r.as_posix() not in IGNORE:
            yield r.as_posix()


def inspect_file(rel):
    """Returns (subtopics, one-line hint) pulled from the file itself."""
    p = ROOT / rel
    if p.suffix == ".py":
        try:
            tree = ast.parse(p.read_text(encoding="utf-8", errors="ignore"))
            names = [n.name for n in tree.body if isinstance(n, (ast.FunctionDef, ast.ClassDef))]
            doc = (ast.get_docstring(tree) or "").strip().splitlines()
            return names[:6], (doc[0] if doc else "")
        except SyntaxError:
            return [], ""
    if p.suffix == ".md":
        for line in p.read_text(encoding="utf-8", errors="ignore").splitlines():
            if line.startswith("#"):
                return [], line.lstrip("# ").strip()
    return [], ""


def pretty(rel):
    stem = Path(rel).stem.replace("_", " ").replace("-", " ").strip()
    return stem[:1].upper() + stem[1:]


claimed = {t["file"] for tr in tracks for c in tr["chapters"] for t in c["topics"] if t.get("file")}
for tr in tracks:
    for ch in tr["chapters"]:
        folder = ch.get("autofolder")
        if not folder or not (ROOT / folder).is_dir():
            continue
        for rel in rel_files(ROOT / folder):
            if rel in claimed:
                continue
            subs, hint = inspect_file(rel)
            ch["topics"].append({"name": pretty(rel), "status": ch.get("autostatus", "done"), "subtopics": subs,
                                 "future": hint or ch.get("autofuture", ""), "file": rel})
            claimed.add(rel)

unmapped = [r for r in rel_files(ROOT)
            if r not in claimed and not any(r.startswith(c.rstrip("/") + "/") for c in claimed)]
for t in tracks:
    t["pct"] = pct(topics(t))
all_topics = [x for t in tracks for x in topics(t)]
overall = pct(all_topics)
n_done = sum(x["status"] == "done" for x in all_topics)

# ---------- animated SVG dashboard ----------
W, ROW, TOP, BX, BW = 860, 44, 96, 250, 480
H = TOP + ROW * len(tracks) + 24
rows = []
for i, t in enumerate(tracks):
    y = TOP + i * ROW
    c = COLORS[i % len(COLORS)]
    w = max(t["pct"] / 100 * BW, 0)
    delay = 0.15 * i
    dot = ""
    if 0 < t["pct"] < 100:
        dot = (f'<circle cx="{BX + w:.1f}" cy="{y + 9}" r="5" fill="{c}">'
               f'<animate attributeName="r" values="4;9;4" dur="1.8s" repeatCount="indefinite"/>'
               f'<animate attributeName="opacity" values="1;.3;1" dur="1.8s" repeatCount="indefinite"/></circle>')
    bar = (f'<rect class="bar" x="{BX}" y="{y}" width="{w:.1f}" height="18" rx="9" fill="{c}" '
           f'style="animation-delay:{delay + .3:.2f}s"/>') if w else ""
    done_n = sum(x["status"] == "done" for x in topics(t))
    rows.append(f'''
  <g class="row" style="animation-delay:{delay:.2f}s">
    <text x="28" y="{y + 14}" class="lbl">{t.get("emoji", "")} {escape(t["name"])}</text>
    <rect x="{BX}" y="{y}" width="{BW}" height="18" rx="9" class="track"/>
    {bar}{dot}
    <text x="{BX + BW + 18}" y="{y + 14}" class="pct" fill="{c}">{t["pct"]}%</text>
    <text x="{BX + BW + 62}" y="{y + 14}" class="sub">{done_n}/{len(topics(t))}</text>
  </g>''')
C = 2 * 3.14159 * 34
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Journey dashboard: {overall}% overall">
<style>
  :root {{ --card:#f6f8fa; --line:#d0d7de; --txt:#1f2328; --mute:#656d76; --track:#e6eaef; }}
  @media (prefers-color-scheme: dark) {{ :root {{ --card:#161b22; --line:#30363d; --txt:#e6edf3; --mute:#8b949e; --track:#262c36; }} }}
  text {{ font-family:-apple-system,'Segoe UI',Helvetica,Arial,sans-serif; }}
  .lbl {{ font-size:15px; fill:var(--txt); font-weight:600 }}
  .pct {{ font-size:15px; font-weight:800 }}
  .sub {{ font-size:12px; fill:var(--mute) }}
  .track {{ fill:var(--track) }}
  .bar {{ transform-box:fill-box; transform-origin:left center; animation:grow 1.3s cubic-bezier(.2,.8,.2,1) both }}
  .row {{ animation:fade .7s ease both }}
  .ring {{ stroke-dasharray:{C:.2f}; stroke-dashoffset:{C * (1 - overall / 100):.2f}; transform:rotate(-90deg); transform-origin:{W - 72}px 48px; animation:ring 1.8s cubic-bezier(.2,.8,.2,1) both }}
  @keyframes grow {{ from {{ transform:scaleX(0) }} }}
  @keyframes fade {{ from {{ opacity:0; transform:translateY(8px) }} }}
  @keyframes ring {{ from {{ stroke-dashoffset:{C:.2f} }} }}
</style>
<rect width="{W}" height="{H}" rx="18" fill="var(--card)" stroke="var(--line)"/>
<text x="28" y="40" style="font-size:22px;font-weight:800;fill:var(--txt)">Journey Dashboard</text>
<text x="28" y="64" class="sub" style="font-size:13px">Checkpoint: {escape(data["checkpoint"])}  ·  {n_done}/{len(all_topics)} topics complete</text>
<circle cx="{W - 72}" cy="48" r="34" fill="none" stroke="var(--track)" stroke-width="9"/>
<circle class="ring" cx="{W - 72}" cy="48" r="34" fill="none" stroke="#22c55e" stroke-width="9" stroke-linecap="round"/>
<text x="{W - 72}" y="54" text-anchor="middle" style="font-size:18px;font-weight:800;fill:var(--txt)">{overall}%</text>
{''.join(rows)}
</svg>'''
(ROOT / "assets").mkdir(exist_ok=True)
(ROOT / "assets" / "dashboard.svg").write_text(svg, encoding="utf-8")
ver = hashlib.md5(svg.encode()).hexdigest()[:8]  # cache-buster so GitHub refreshes the image


# ---------- markdown blocks ----------
def mdbar(p, n=20):
    f = round(p / 100 * n)
    return "█" * f + "░" * (n - f)


plain = "\n".join(f'{t["name"]:<22}[{mdbar(t["pct"], 10)}] {t["pct"]:>3}%' for t in tracks)
dash = (f'<p align="center"><img src="assets/dashboard.svg?v={ver}" alt="Journey dashboard" width="100%"/></p>\n\n'
        f'**Current checkpoint:** `{data["checkpoint"]}`  \n**Overall:** `{mdbar(overall)}` **{overall}%**\n\n'
        f'<details><summary>Plain-text view</summary>\n\n```text\n{plain}\n```\n</details>')

ids = [f"t{i}" for i in range(len(tracks))]
mm = ["```mermaid", "flowchart LR"]
for i, t in enumerate(tracks):
    mm.append(f'    {ids[i]}["{t.get("emoji", "")} {t["name"]}<br/>{t["pct"]}%"]')
mm.append("    " + " --> ".join(ids))
mm += ["    classDef done fill:#bbf7d0,stroke:#166534,color:#052e16;",
       "    classDef current fill:#fde68a,stroke:#92400e,color:#451a03,stroke-width:3px;",
       "    classDef future fill:#e0f2fe,stroke:#075985,color:#082f49;"]
for kind, cond in (("done", lambda p: p == 100), ("current", lambda p: 0 < p < 100), ("future", lambda p: p == 0)):
    sel = [ids[i] for i, t in enumerate(tracks) if cond(t["pct"])]
    if sel:
        mm.append(f'    class {",".join(sel)} {kind};')
mm.append("```")
mm.append("\n🟢 complete · 🟡 in progress · 🔵 upcoming")
mapmd = "\n".join(mm)

book, ch_no, index = [], 0, {}
for pi, t in enumerate(tracks, 1):
    book.append(f'### Part {pi} · {t.get("emoji", "")} {t["name"]} — {t["pct"]}%\n')
    for ch in t["chapters"]:
        ch_no += 1
        done = sum(x["status"] == "done" for x in ch["topics"])
        is_open = " open" if 0 < t["pct"] < 100 else ""
        book.append(f'<details{is_open}>\n<summary><b>Chapter {ch_no}: {escape(ch["title"])}</b> &nbsp;·&nbsp; {done}/{len(ch["topics"])} topics</summary>\n')
        book.append(f'_{ch["summary"]}_\n')
        book.append("| | Topic | Source | Subtopics covered | Future reference (AI / backend) |\n| :-: | --- | --- | --- | --- |")
        for x in ch["topics"]:
            index[x["name"].lower()] = f"Ch.{ch_no}"
            subs = ", ".join(x["subtopics"]) or "—"
            src = f'[`{x["file"].split("/")[-1]}`]({x["file"]})' if x.get("file") else "—"
            book.append(f'| {ICON[x["status"]]} | **{cell(x["name"])}** | {src} | {cell(subs)} | {cell(x["future"] or "—")} |')
        book.append("\n</details>\n")
if unmapped:
    book.append("<details><summary><b>📂 Not yet catalogued</b> — files in the repo that no chapter claims yet</summary>\n")
    book += [f"- [`{u}`]({u})" for u in unmapped]
    book.append("\n</details>\n")
    print("Uncatalogued files:", *unmapped, sep="\n  ")
bookmd = "\n".join(book)

projs = data.get("projects", [])
if not projs:
    pm = "_No projects yet. Add one to `journey.json` under `projects` and this table fills itself in._"
else:
    rows_md = ["| Project | Status | Concepts used (chapter) |", "| --- | --- | --- |"]
    for p in projs:
        used = ", ".join(f'`{c}` ({index.get(c.lower(), "?")})' for c in p["concepts"])
        name = f'[{p["name"]}]({p["link"]})' if p.get("link") else p["name"]
        rows_md.append(f'| {name} | {p.get("status", "building")} | {used} |')
    pm = "\n".join(rows_md)

readme = ROOT / "README.md"
text = readme.read_text(encoding="utf-8")
for tag, body in (("DASH", dash), ("MAP", mapmd), ("BOOK", bookmd), ("PROJECTS", pm)):
    text = re.sub(rf"(<!--{tag}:START-->).*?(<!--{tag}:END-->)",
                  lambda m, b=body: f"{m.group(1)}\n{b}\n{m.group(2)}", text, flags=re.S)
readme.write_text(text, encoding="utf-8")
print(f"README updated: overall {overall}%, {len(all_topics)} topics, {ch_no} chapters")
