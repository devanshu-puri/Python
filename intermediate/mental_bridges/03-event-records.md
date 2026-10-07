# Module 3 — Clean a Batch of Event Records

## 1. Real-World Scenario

A service receives a small batch of event dictionaries. Some entries are
incomplete; the useful ones need to be counted and shown in time order.

## 2. The Challenge

Keep records with an `event` and `user`, count event names, then sort the valid
records by their `time` value.

## 3. My Current Python Toolkit

- Lists and dictionaries model a batch of records.
- A function names the cleanup rule; a comprehension filters records.
- A dictionary can count frequencies; `sorted(key=...)` orders results.

## 4. Think Before Coding

- Should a missing field be ignored or treated as an error?
- Is `time` guaranteed to have a consistent format?
- Should the original input list be changed?

## 5. Try It Yourself

```python
events = [
    {"user": "ari", "event": "login", "time": 3},
    {"user": "bo", "event": "view", "time": 1},
    {"event": "login", "time": 2},
]
```

Clean, count, and sort these records without modifying `events`.

## 6. Solution

### Version A — Straightforward Python

```python
def valid(record):
    return "user" in record and "event" in record and "time" in record

clean = []
for record in events:
    if valid(record):
        clean.append(record)
counts = {}
for record in clean:
    event = record["event"]
    counts[event] = counts.get(event, 0) + 1
ordered = sorted(clean, key=lambda record: record["time"])
```

### Version B — Pythonic implementation

```python
clean = [r for r in events if all(k in r for k in ("user", "event", "time"))]
counts = {name: sum(r["event"] == name for r in clean)
          for name in {r["event"] for r in clean}}
ordered = sorted(clean, key=lambda r: r["time"])
```

Version A makes counting easy to follow and does one pass. Version B shows
useful built-ins, but the frequency comprehension scans records repeatedly;
clarity and efficiency matter more than shortening the code.

## 7. Trace It Visually

```text
3 input records -> validation -> 2 valid records
valid events: login, view
counts:        login: 1, view: 1
sort by time:  view(time=1), login(time=3)
```

## 8. What Is Actually Happening Internally?

The comprehension builds a new list. `sorted()` also returns a new list;
its `key` function supplies the value used for each comparison.

## 9. THE IMPORTANT PART — "THIS BECOMES..."

### Python

Filter, count, and sort dictionaries.

↓

### Backend

Summarize request, payment, or audit events.

↓

### Production

Validate schemas, handle large files incrementally, and report bad rows.

↓

### AI / LLM

Normalize model outputs and count categories or tool outcomes.

↓

### Advanced System

Event pipelines transform records before analytics. [LEARN LATER] For large
streams, generators or queues avoid loading every record at once.

## 10. Future Code Example

```python
def event_summary(records):
    counts = {}
    for record in records:
        name = record.get("event", "unknown")
        counts[name] = counts.get(name, 0) + 1
    return counts
```

Underlying basics: function, loop, dictionary, `.get()`, and reassignment.

## 11. "Mind-Bending" Questions

1. Why is checking `record["user"]` unsafe before checking the key exists?
2. Does `sorted()` change `events`?
3. Why can the counting comprehension be slower for many records?
4. What if `time` is a string in one record and a number in another?
5. When should a bad record raise an error instead of being skipped?

### Answers

1. A missing key raises `KeyError`.
2. No; it creates a sorted list. `list.sort()` changes that list in place.
3. It scans the valid records for each distinct event name.
4. Sorting may fail or produce an unintended ordering; normalize the data first.
5. When skipping would hide a broken contract or cause incorrect results.

## 12. Interview Connection

- One-pass counting with a dictionary.
- `sorted(iterable, key=...)` versus in-place `.sort()`.
- Time/space tradeoffs and input validation.

## 13. Common Mistakes

**WRONG:** `ordered = events.sort(key=...)`  
**WHY:** `.sort()` returns `None` and changes the list in place.  
**CORRECT:** Use `events.sort(...)` or `ordered = sorted(events, key=...)`.

**WRONG:** `record["event"]` before checking the record.  
**WHY:** A missing key raises `KeyError`.  
**CORRECT:** Validate required fields or use `.get()` for optional fields.

## 14. Small Extension

- Load a JSON array with `json.load()` and process it.
- Keep invalid records in a separate list with a reason.
- Group valid records by user before counting events.

## 15. Connection Graph

List of dicts → validate and transform records → API/event summaries → clean
model outputs and retrieval metadata.
