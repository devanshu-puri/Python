"""Module 3 - Filter users with conditions and comprehensions."""

# 1. Real-World Scenario
# An operations page should show active users who belong to the backend team.

# 2. The Challenge
users = [
    {'name': 'Ava', 'team': 'backend', 'active': True},
    {'name': 'Sam', 'team': 'ai', 'active': True},
    {'name': 'Mia', 'team': 'backend', 'active': False},
]
# Return names matching both conditions.

# 3. My Current Python Toolkit
# Lists hold records, dictionaries hold fields, and conditions decide inclusion.

# 4. Think Before Coding
# What should happen when a field is missing? Is filtering or transforming the goal?

# 5. Try It Yourself
# Build the list of names without changing users.

# 6. Solution

active_backend_a = []
for user in users:
    if user.get('active') and user.get('team') == 'backend':
        active_backend_a.append(user['name'])
print('Version A:', active_backend_a)

active_backend_b = [
    user['name'] for user in users
    if user.get('active') and user.get('team') == 'backend'
]
print('Version B:', active_backend_b)
# The comprehension is good for one simple condition; use a loop for multi-step logic.

# 7. Trace It Visually
# Ava: active + backend -> keep Ava.
# Sam: active + ai -> discard.
# Mia: inactive + backend -> discard.

# 8. What Is Actually Happening Internally?
# The comprehension visits each dictionary, evaluates the condition, then appends only matches.

# 9. THE IMPORTANT PART - THIS BECOMES...
# Python: filter records by fields
# Backend: filter users or orders for an endpoint response
# Production: validate filters, pagination, and database-side filtering
# AI / LLM: filter documents by metadata before retrieval
# Advanced System: access-controlled retrieval [LEARN LATER]

# 10. Future Code Example
chunks = [
    {'text': 'billing policy', 'tenant': 'acme', 'approved': True},
    {'text': 'internal note', 'tenant': 'other', 'approved': True},
]
visible = [chunk for chunk in chunks if chunk['tenant'] == 'acme' and chunk['approved']]
print('Visible chunks:', visible)

# 11. Mind-Bending Questions
questions = [
    'Why does get() avoid a KeyError here?',
    'What if active is the string "False"?',
    'How would you return full dictionaries instead of names?',
    'Would filtering in Python always be efficient for one million records?',
    'Can metadata filtering alone enforce security?',
]
for number, question in enumerate(questions, 1):
    print(f'Q{number}: {question}')

# Answers
print('Answers: get supplies a safe missing value; strings are truthy; remove user[\'name\']; large data belongs closer to storage; enforce identity and policy too.')

# 12. Interview Connection
print('Interview: comprehensions, truthiness, missing keys, predicate functions, and filtering cost.')

# 13. Common Mistakes
# WRONG: [user for user in users if user['active'] == True and user['team'] == 'backend']
# CORRECT: [user for user in users if user.get('active') and user.get('team') == 'backend']
# WRONG: users.remove(user) while iterating over users.
# CORRECT: create a new filtered list.

# 14. Small Extension
# Add a role filter, a name search, and a limit for the first five results.

# 15. Connection Graph
# list + dict -> predicate -> filtered records -> API query -> metadata filtering -> safe RAG context
