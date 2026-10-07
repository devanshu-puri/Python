# Module 2 — Check Access Without Guessing

## 1. Real-World Scenario

A small service lets users open certain actions. Each user has a collection of
allowed actions, and a request asks whether one action is allowed.

## 2. The Challenge

Represent permissions and write a function that checks membership. Try an
unknown user and a misspelled action.

## 3. My Current Python Toolkit

- Dictionaries map a user to that user's permission collection.
- Sets represent unique permission labels.
- `in` checks membership; a function makes the rule reusable.

## 4. Think Before Coding

- Should permissions allow duplicates?
- What should happen when the user is unknown?
- Is this demo enough to secure a real API?

## 5. Try It Yourself

```python
permissions = {
    "ari": {"read", "publish"},
    "bo": {"read"},
}
```

Implement `allowed(user, action)` and test allowed, denied, and unknown cases.

## 6. Solution

### Version A — Straightforward Python

```python
def allowed(user, action):
    if user not in permissions:
        return False
    return action in permissions[user]
```

### Version B — Pythonic implementation

```python
def allowed(user, action):
    return action in permissions.get(user, set())
```

The concise form is fine for this demo. In a real authorization system,
distinguish an unknown user from a known user with no permission; do not treat
this in-memory example as authentication.

## 7. Trace It Visually

```text
user "ari" -> {"read", "publish"}
action "publish" -> membership test -> True
user "bo"  -> {"read"}
action "publish" -> membership test -> False
```

## 8. What Is Actually Happening Internally?

A set stores unique hashable values. Membership asks whether an equal item is
present; set lookup is typically efficient, especially when repeated often.

## 9. THE IMPORTANT PART — "THIS BECOMES..."

### Python

Set membership decides whether a label exists.

↓

### Backend

Check whether an authenticated identity may perform an action.

↓

### Production

Permission rules may depend on resource, tenant, and current policy.

↓

### AI / LLM

Decide which tools or documents a user may access.

↓

### Advanced System

Filter retrieval results by tenant and access policy. [LEARN LATER] A model's
answer must not replace an application's authorization check.

## 10. Future Code Example

```python
def visible_documents(user, documents):
    return [
        doc for doc in documents
        if doc["tenant"] == user["tenant"]
        and doc["id"] in user["allowed_docs"]
    ]
```

Underlying basics: list iteration, dict lookup, `and`, and set membership.

## 11. "Mind-Bending" Questions

1. Why use a set rather than a list for repeated membership checks?
2. What does `.get(user, set())` return for an unknown user?
3. Can a user name alone prove that a request is authorized?
4. What if a permission is misspelled?
5. Why check document access before sending text to an LLM?

### Answers

1. Sets are designed for unique items and typically make membership checks
   efficient.
2. An empty set, so the check returns `False`.
3. No. Identity must be established separately, and access rules must be checked.
4. The check usually returns `False`; validate permission labels to catch typos.
5. To avoid disclosing text the user is not allowed to see.

## 12. Interview Connection

- Set membership and uniqueness.
- Authentication answers "who?"; authorization answers "allowed to do what?"
- Security checks belong at the trusted application boundary.

## 13. Common Mistakes

**WRONG:** `if action in permissions:`  
**WHY:** That checks usernames, not the selected user's actions.  
**CORRECT:** `action in permissions.get(user, set())`

**WRONG:** Let the LLM decide if the user is allowed.  
**WHY:** Model output is not a security boundary.  
**CORRECT:** Enforce permission checks in ordinary application code.

## 14. Small Extension

- Add a resource ID to the permission check.
- Store permissions by role, then map users to roles.
- Return separate results for "unknown user" and "not allowed".

## 15. Connection Graph

Set + `in` → membership rule → API authorization → tenant/resource policy →
RAG document and assistant-tool access checks.
