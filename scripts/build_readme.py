#!/usr/bin/env python3
"""Rebuild the generated parts of the repo from journey.json.

Generates
  * README.md              dashboard, learning map, track table, book, projects
  * assets/dashboard.svg   progress card used by the README
  * <area>/README.md       one per entry under "areas" (01-python, 02-backend, ...)

Only the text between <!--NAME:START--> and <!--NAME:END--> markers is replaced,
so anything you write around the markers is safe.

Usage:
    python scripts/build_readme.py            # rebuild
    python scripts/build_readme.py --strict   # exit 1 if there are warnings
"""
from __future__ import annotations

import fnmatch
import hashlib
import json
import os
import re
import sys
from html import escape
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
JOURNEY = ROOT / "journey.json"
README = ROOT / "README.md"
DASHBOARD = ROOT / "assets" / "dashboard.svg"

ICON = {"done": "✅", "wip": "🟡", "todo": "⬜"}
WEIGHT = {"done": 1.0, "wip": 0.5, "todo": 0.0}  # wip counts as half
PROJECT_ICON = {"done": "✅", "building": "🛠️", "planned": "💡"}

AREA_TEMPLATE = """# {emoji} {num} · {title}

<!--AUTO:START-->
<!--AUTO:END-->

---

⬅️ Back to the [main roadmap](../README.md)
"""

warnings: list[str] = []


# --------------------------------------------------------------------------- helpers
def warn(message: str) -> None:
    warnings.append(message)


def percent(score: float, total: int) -> int:
    return int(100 * score / total + 0.5) if total else 0


def bar(pct: int, width: int = 20) -> str:
    filled = round(width * pct / 100)
    return "█" * filled + "░" * (width - filled)


def stats(topics: list[dict]) -> tuple[int, int, int]:
    """(done, total, percent) for a list of topics."""
    done = sum(t["status"] == "done" for t in topics)
    score = sum(WEIGHT[t["status"]] for t in topics)
    return done, len(topics), percent(score, len(topics))


def chapter_topics(chapters: list[dict]) -> list[dict]:
    return [t for ch in chapters for t in ch["topics"]]


def topic_files(topic: dict) -> list[str]:
    files = [topic["file"]] if topic.get("file") else []
    return files + topic.get("also", [])


def rel(path: str, base: Path = ROOT) -> str:
    """Link from `base` (a folder) to a repo-root-relative `path`."""
    return quote(Path(os.path.relpath(ROOT / path, base)).as_posix())


def cell(text: object) -> str:
    return str(text).replace("|", "\\|").replace("\n", " ").strip() or "—"


def leading_number(name: str) -> int | None:
    match = re.match(r"(\d+)", name)
    return int(match.group(1)) if match else None


def chapter_num(chapter: dict) -> str:
    """'01-basics' -> '01'"""
    n = leading_number(Path(chapter.get("folder", "")).name)
    return f"{n:02d}" if n is not None else "·"


def chapter_label(chapter: dict) -> str:
    """'01-python/03-oop' -> '1.3'"""
    parts = Path(chapter.get("folder", "")).parts
    if len(parts) >= 2:
        a, c = leading_number(parts[0]), leading_number(parts[1])
        if a is not None and c is not None:
            return f"{a}.{c}"
    return "?"


def in_progress(topics: list[dict]) -> bool:
    done, total, _ = stats(topics)
    return any(t["status"] == "wip" for t in topics) or 0 < done < total


def area_chapters(data: dict, area: dict) -> list[dict]:
    prefix = area["path"].rstrip("/") + "/"
    chapters = [
        ch
        for track in data["tracks"]
        for ch in track["chapters"]
        if ch.get("folder", "").startswith(prefix)
    ]
    return sorted(chapters, key=lambda c: c["folder"])


def write(path: Path, text: str) -> bool:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.read_text(encoding="utf-8") == text:
        return False
    path.write_text(text, encoding="utf-8", newline="\n")
    return True


def replace_block(text: str, name: str, new: str, where: str) -> str:
    pattern = re.compile(rf"(<!--{name}:START-->)(.*?)(<!--{name}:END-->)", re.S)
    if not pattern.search(text):
        warn(f"{where} has no <!--{name}:START--> / <!--{name}:END--> markers")
        return text
    return pattern.sub(lambda m: f"{m.group(1)}\n{new}\n{m.group(3)}", text)


# --------------------------------------------------------------------------- validation
def validate(data: dict) -> dict[str, tuple[dict, dict, dict]]:
    """Check statuses; return {topic name: (track, chapter, topic)}."""
    names: dict[str, tuple[dict, dict, dict]] = {}
    for track in data["tracks"]:
        for chapter in track["chapters"]:
            if not chapter.get("folder"):
                warn(f"chapter '{chapter['title']}' has no \"folder\"")
            for topic in chapter["topics"]:
                if topic["status"] not in WEIGHT:
                    sys.exit(f"Bad status {topic['status']!r} on '{topic['name']}' (use done / wip / todo)")
                if topic["name"] in names:
                    warn(f"duplicate topic name: {topic['name']}")
                names[topic["name"]] = (track, chapter, topic)
    return names


def check_files(data: dict) -> None:
    referenced: set[str] = set()
    for track in data["tracks"]:
        for chapter in track["chapters"]:
            for topic in chapter["topics"]:
                for f in topic_files(topic):
                    referenced.add(f)
                    if topic["status"] != "todo" and not (ROOT / f).exists():
                        warn(f"missing file for '{topic['name']}': {f}")
    for project in data.get("projects", []):
        if project.get("path") and not (ROOT / project["path"]).exists():
            warn(f"missing project folder for '{project['name']}': {project['path']}")
    ignore = data.get("ignore", [])
    for area in data.get("areas", []):
        base = ROOT / area["path"]
        if not base.is_dir():
            continue
        for p in sorted(base.rglob("*.py")):
            relative = p.relative_to(ROOT).as_posix()
            if relative in referenced or "__pycache__" in p.parts:
                continue
            if any(fnmatch.fnmatch(relative, pattern) for pattern in ignore):
                continue
            warn(f"file not listed in journey.json: {relative}")


# --------------------------------------------------------------------------- tables
def source_cell(topic: dict, base: Path) -> str:
    files = topic_files(topic)
    if not files:
        return "—"
    return "<br>".join(f"[`{Path(f).name}`]({rel(f, base)})" for f in files)


def topic_table(topics: list[dict], base: Path, numbered: bool) -> str:
    """Render topics as compact checklist items; wide tables are poor on phones."""
    lines = []
    for i, t in enumerate(topics, 1):
        mark = {"done": "x", "wip": "/", "todo": " "}.get(t["status"], " ")
        title = f"**{cell(t['name'])}**"
        if numbered:
            title = f"**{i:02d}. {cell(t['name'])}**"
        details = []
        if t.get("subtopics"):
            details.append(", ".join(cell(x) for x in t["subtopics"]))
        files = topic_files(t)
        if files:
            details.append("Source: " + ", ".join(f"[`{Path(f).name}`]({rel(f, base)})" for f in files))
        line = f"- [{mark}] {title}"
        if details:
            line += "  —  " + " · ".join(details)
        if t.get("future"):
            line += f"\n  - *Why it matters later:* {cell(t['future'])}"
        lines.append(line)
    return "\n".join(lines) if lines else "_Topics will be added here._"


def project_table(projects: list[dict], names: dict, base: Path) -> str:
    lines = []
    for pr in projects:
        target = pr.get("link") or (rel(pr["path"], base) if pr.get("path") else None)
        label = f"[**{cell(pr['name'])}**]({target})" if target else f"**{cell(pr['name'])}**"
        status = pr.get("status", "planned")
        icon = PROJECT_ICON.get(status, "💡")
        lines.append(f"- {icon} {label} — *{status}*")
        if pr.get("summary"):
            lines.append(f"  - {cell(pr['summary'])}")
        concepts = []
        for name in pr.get("concepts", []):
            hit = names.get(name)
            if hit:
                concepts.append(f"{cell(name)} _({cell(hit[1]['title'])})_")
            else:
                warn(f"project '{pr['name']}' uses unknown concept '{name}'")
                concepts.append(cell(name))
        if concepts:
            lines.append("  - **Concepts:** " + ", ".join(concepts))
    return "\n".join(lines) if lines else "_No projects yet._"


# --------------------------------------------------------------------------- main README blocks
def build_svg(rows: list[dict], overall: int, checkpoint: str) -> str:
    width, pad = 900, 36
    bar_x, bar_w, row_h, top = 270, 520, 40, 160
    height = top + row_h * len(rows) + 4
    font = 'font-family="ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif"'

    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-label="Learning journey dashboard">',
        f'<rect width="{width}" height="{height}" rx="18" fill="#0f172a"/>',
        f'<text x="{pad}" y="54" {font} font-size="24" font-weight="700" fill="#f8fafc">Journey Dashboard</text>',
        f'<text x="{pad}" y="80" {font} font-size="13" fill="#94a3b8">Checkpoint: {escape(checkpoint)}</text>',
        f'<text x="{pad}" y="116" {font} font-size="15" font-weight="700" fill="#f8fafc">Overall</text>',
        f'<rect x="{bar_x}" y="104" width="{bar_w}" height="16" rx="8" fill="#1e293b"/>',
    ]
    if overall:
        out.append(f'<rect x="{bar_x}" y="104" width="{max(bar_w * overall / 100, 16):.1f}" height="16" rx="8" fill="#8b5cf6"/>')
    out.append(f'<text x="{width - pad}" y="117" {font} font-size="15" font-weight="700" fill="#f8fafc" text-anchor="end">{overall}%</text>')
    out.append(f'<line x1="{pad}" y1="136" x2="{width - pad}" y2="136" stroke="#1e293b" stroke-width="2"/>')

    for i, row in enumerate(rows):
        cy = top + i * row_h
        pct = row["pct"]
        color = "#22c55e" if pct == 100 else "#f59e0b"
        out.append(f'<text x="{pad}" y="{cy + 5}" {font} font-size="14" fill="#e2e8f0">{escape(row["track"]["name"])}</text>')
        out.append(f'<rect x="{bar_x}" y="{cy - 6}" width="{bar_w}" height="12" rx="6" fill="#1e293b"/>')
        if pct:
            out.append(f'<rect x="{bar_x}" y="{cy - 6}" width="{max(bar_w * pct / 100, 12):.1f}" height="12" rx="6" fill="{color}"/>')
        out.append(f'<text x="{width - pad}" y="{cy + 5}" {font} font-size="14" fill="#cbd5e1" text-anchor="end">{pct}%</text>')
    out.append("</svg>")
    return "\n".join(out) + "\n"


def build_dash(rows: list[dict], overall: int, checkpoint: str) -> tuple[str, str]:
    svg = build_svg(rows, overall, checkpoint)
    version = hashlib.md5(svg.encode("utf-8")).hexdigest()[:8]
    width = max(len(r["track"]["name"]) for r in rows) + 2
    plain = "\n".join(f"{r['track']['name']:<{width}}[{bar(r['pct'], 10)}] {r['pct']:>3}%" for r in rows)
    block = (
        f'<p align="center"><img src="assets/dashboard.svg?v={version}" alt="Journey dashboard" width="100%"/></p>\n\n'
        f"**Current checkpoint:** `{checkpoint}`  \n"
        f"**Overall:** `{bar(overall)}` **{overall}%**\n\n"
        f"<details><summary>Plain-text view</summary>\n\n```text\n{plain}\n```\n</details>"
    )
    return svg, block


def build_map(rows: list[dict]) -> str:
    lines = ["A quick view of what is complete, in progress, and still ahead:", ""]
    for r in rows:
        t = r["track"]
        status = "🟢" if r["pct"] == 100 else "🟡" if r["pct"] > 0 else "🔵"
        lines.append(f"- {status} **{t['emoji']} {cell(t['name'])}** — {r['pct']}% ({r['done']}/{r['total']} topics)")
    lines += ["", "🟢 Complete · 🟡 In progress · 🔵 Upcoming"]
    return "\n".join(lines)


def build_areas_table(data: dict) -> str:
    blocks = []
    for area in data.get("areas", []):
        d, t, p = stats(chapter_topics(area_chapters(data, area)))
        folder = area["path"]
        blocks += [
            f"<details>",
            f"<summary><b>{area['emoji']} {cell(area['title'])}</b> · {p}% · {d}/{t} topics</summary>",
            "",
            area["summary"],
            "",
            f"📁 [`{folder}/`]({quote(folder)}/)",
            "",
            "</details>",
            "",
        ]
    return "\n".join(blocks).rstrip()


def build_book(data: dict) -> str:
    out: list[str] = []
    for part, track in enumerate(data["tracks"], 1):
        _, _, pct = stats(chapter_topics(track["chapters"]))
        out.append(f"### Part {part} · {track['emoji']} {track['name']} — {pct}%\n")
        for chapter in track["chapters"]:
            done, total, _ = stats(chapter["topics"])
            folder = chapter.get("folder", "")
            folder_link = f" · 📂 [`{folder}/`]({quote(folder)})" if folder else ""
            out.append("<details>")
            out.append(f"<summary><b>{chapter_label(chapter)} · {escape(chapter['title'])}</b> — {done}/{total} topics</summary>")
            out.append("")
            out.append(f"_{chapter['summary']}_{folder_link}")
            out.append("")
            out.append(topic_table(chapter["topics"], ROOT, numbered=False))
            out.append("")
            out.append("</details>")
            out.append("")
    return "\n".join(out).rstrip()


def build_projects_block(data: dict, names: dict) -> str:
    projects = data.get("projects", [])
    if not projects:
        return "_No projects yet. Add one to `journey.json` under `projects` and this table fills itself in._"
    return project_table(projects, names, ROOT)


# --------------------------------------------------------------------------- area READMEs
def build_area_block(area: dict, data: dict, names: dict) -> str:
    chapters = area_chapters(data, area)
    base = ROOT / area["path"]
    done, total, pct = stats(chapter_topics(chapters))

    out = [
        f"> {area['summary']}",
        "",
        f"**Progress:** `{bar(pct)}` **{pct}%** · {done} of {total} topics done",
        "",
    ]
    if area.get("how_to_study"):
        out += ["## 🧭 How to use this folder", "", area["how_to_study"], ""]

    out += ["## 📚 Chapters", ""]
    for ch in chapters:
        d, t, _ = stats(ch["topics"])
        out += [
            f"### {chapter_num(ch)} · {ch['title']}",
            "",
            f"_{ch['summary']}_ · {d}/{t} topics done",
            "",
            topic_table(ch["topics"], base, numbered=True),
            "",
        ]

    prefix = area["path"].rstrip("/") + "/"
    projects = [p for p in data.get("projects", []) if p.get("path", "").startswith(prefix)]
    if projects:
        out += ["## 🧪 Projects in this folder", "", project_table(projects, names, base), ""]

    out.append("✅ done · 🟡 in progress · ⬜ not started")
    return "\n".join(out)


def write_area_readme(area: dict, data: dict, names: dict) -> bool:
    path = ROOT / area["path"] / "README.md"
    if path.exists():
        text = path.read_text(encoding="utf-8")
    else:
        num = leading_number(area["path"])
        text = AREA_TEMPLATE.format(
            emoji=area["emoji"], num=f"{num:02d}" if num is not None else "", title=area["title"]
        )
    text = replace_block(text, "AUTO", build_area_block(area, data, names), f"{area['path']}/README.md")
    return write(path, text)


# --------------------------------------------------------------------------- main
def main() -> int:
    strict = "--strict" in sys.argv
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")  # emoji on Windows consoles

    data = json.loads(JOURNEY.read_text(encoding="utf-8"))
    names = validate(data)

    rows = []
    for track in data["tracks"]:
        d, t, p = stats(chapter_topics(track["chapters"]))
        rows.append({"track": track, "done": d, "total": t, "pct": p})
    everything = chapter_topics([ch for tr in data["tracks"] for ch in tr["chapters"]])
    _, _, overall = stats(everything)

    svg, dash = build_dash(rows, overall, data["checkpoint"])
    blocks = {
        "DASH": dash,
        "MAP": build_map(rows),
        "AREAS": build_areas_table(data),
        "BOOK": build_book(data),
        "PROJECTS": build_projects_block(data, names),
    }

    if not README.exists():
        sys.exit("README.md not found. Copy the template README.md into the repo root first.")
    text = README.read_text(encoding="utf-8")
    for name, block in blocks.items():
        text = replace_block(text, name, block, "README.md")

    changed = []
    if write(DASHBOARD, svg):
        changed.append(DASHBOARD.relative_to(ROOT).as_posix())
    if write(README, text):
        changed.append("README.md")
    for area in data.get("areas", []):
        if write_area_readme(area, data, names):
            changed.append(f"{area['path']}/README.md")

    check_files(data)

    print(f"Overall progress: {overall}%")
    print("Updated: " + ", ".join(changed) if changed else "Everything already up to date.")
    if warnings:
        print(f"\n{len(warnings)} warning(s):")
        for w in warnings:
            print(f"  - {w}")
    return 1 if (strict and warnings) else 0


if __name__ == "__main__":
    sys.exit(main())