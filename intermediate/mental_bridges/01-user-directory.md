# Module 1 — Build a Tiny User Directory

## 1. Real-World Scenario

An app receives usernames and role names as two lists. It needs a lookup by
username and a list of users who can administer the app.

## 2. The Challenge

Pair the usernames and roles, make a dictionary, find admins, and display each
user with their position. Decide what unequal list lengths should mean.

## 3. My Current Python Toolkit

- Lists hold the incoming ordered values.
- `zip()` pairs values at the same position; a dict gives lookup by name.
- Loops, comprehensions, and `enumerate()` help produce results and positions.

## 4. Think Before Coding

- Can a dictionary keep two roles for the same username?
- What does ordinary `zip()` do if lengths differ?
- Is the position a permanent user ID?

## 5. Try It Yourself

```python
names = ["Ari", "Bo", "Cy"]
roles = ["admin", "reader", "reader"]
```

Create `{"Ari": "admin", ...}`, then produce admin names and numbered labels.

## 6. Solution

### Version A — Straightforward Python

```python
user_roles = {}
for name, role in zip(names, roles):
    user_roles[name] = role
admins = []
for name, role in user_roles.items():
    if role == "admin":
        admins.append(name)
```

### Version B — Pythonic implementation

```python
user_roles = dict(zip(names, roles))
admins = [name for name, role in user_roles.items() if role == "admin"]
labels = [f"{i}: {name}" for i, name in enumerate(names, start=1)]
```

Version B is compact for simple transformations. Version A is easier to extend
with extra checks. Use `zip(..., strict=True)` when unequal lengths are invalid.

## 7. Trace It Visually

```text
names:       Ari       Bo        Cy
roles:       admin     reader    reader
zip:        (Ari,admin) (Bo,reader) (Cy,reader)
dictionary: {"Ari": "admin", "Bo": "reader", "Cy": "reader"}
admins:     ["Ari"]
```

## 8. What Is Actually Happening Internally?

`zip()` yields pairs as you iterate over it. `dict()` consumes those pairs;
repeated keys overwrite earlier values. `enumerate()` yields `(index, value)`.

## 9. THE IMPORTANT PART — "THIS BECOMES..."

### Python

Pair values and create a dictionary.

↓

### Backend

Map a user ID to a role or settings.

↓

### Production

Validate IDs and preserve multiple roles when the data model requires them.

↓

### AI / LLM

Map a document or conversation ID to metadata.

↓

### Advanced System

Tenant-specific access checks for retrieved documents. [LEARN LATER] A position
in a list is not a secure or stable identity.

## 10. Future Code Example

```python
role_by_user = dict(zip(names, roles, strict=True))
def can_manage(user):
    return role_by_user.get(user) == "admin"
print(can_manage("Ari"))  # True
```

Underlying basics: dictionary lookup, function, equality, and boolean result.

## 11. "Mind-Bending" Questions

1. What happens if `names` has more entries than `roles` with ordinary `zip()`?
2. What value remains if `"Ari"` appears twice?
3. Why is `enumerate()` better than maintaining a counter manually?
4. Is a username always a good dictionary key?
5. Should missing roles silently be accepted?

### Answers

1. Ordinary `zip()` stops when the shorter input ends; `strict=True` raises
   `ValueError`.
2. The later role overwrites the earlier dictionary value.
3. It keeps the index and item paired without manual counter updates.
4. Only if usernames are unique and stable; real systems often use a user ID.
5. That is a data rule to choose explicitly; silently truncating may hide bad
   input.

## 12. Interview Connection

- `zip()` truncation versus `zip(strict=True)`.
- Dictionary keys, uniqueness, and expected constant-time lookup.
- Choosing a stable identifier rather than a display label.

## 13. Common Mistakes

**WRONG:** `for i in range(len(names)): role = roles[i]`  
**WHY:** A shorter `roles` list raises `IndexError`.  
**CORRECT:** `for name, role in zip(names, roles, strict=True): ...`

**WRONG:** Assume dict preserves duplicate user entries.  
**WHY:** One key has one value; later assignments replace earlier ones.  
**CORRECT:** Use a list of records or map each key to a list if duplicates matter.

## 14. Small Extension

- Give each user multiple roles: `user -> set of roles`.
- Add `user_id` separately from the display name.
- Reject unknown role labels before creating the mapping.

## 15. Connection Graph

`zip()` + dict → pair and look up data → API user directory → role checks →
tenant/document metadata mapping.
