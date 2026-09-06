"""Module 1 - Pair users with roles using zip and a dictionary."""

# 1. Real-World Scenario
# An access service receives user names and their roles in matching order.

# 2. The Challenge
users = ['ava', 'sam', 'mia']
roles = ['admin', 'editor', 'viewer']
# Build user_to_role, then find all users who can edit content.

# 3. My Current Python Toolkit
# zip pairs related values; dict stores fast key -> value lookups; a loop filters results.

# 4. Think Before Coding
# What happens if the lists have different lengths? What should duplicate roles mean?

# 5. Try It Yourself
# Pause here and build the mapping before reading the solutions.

# 6. Solution
user_to_role_a = {}
for user, role in zip(users, roles):
    user_to_role_a[user] = role
editors_a = [user for user, role in user_to_role_a.items() if role in {'admin', 'editor'}]
print('Version A:', user_to_role_a, editors_a)

user_to_role_b = dict(zip(users, roles))
editors_b = [user for user, role in user_to_role_b.items() if role in {'admin', 'editor'}]
print('Version B:', user_to_role_b, editors_b)
# Version B is concise; Version A is clearer when validation or extra work is needed.

# 7. Trace It Visually
# ava + admin -> {'ava': 'admin'} -> ava is allowed.
# sam + editor -> {'ava': 'admin', 'sam': 'editor'} -> sam is allowed.
# mia + viewer -> complete mapping -> mia is not an editor.

# 8. What Is Actually Happening Internally?
# zip produces pairs lazily and stops at the shortest input. dict consumes each pair.

# 9. THE IMPORTANT PART - THIS BECOMES...
# Python: user -> role mapping
# Backend: authorization lookup in an API request
# Production: tenant_id + user_id -> permissions
# AI / LLM: decide which tools or documents a user may access
# Advanced System: multi-tenant access control [LEARN LATER]

# 10. Future Code Example
request = {'user': 'sam', 'action': 'edit'}
allowed = request['action'] in {'view', 'edit'} and user_to_role_b[request['user']] != 'viewer'
print('Future authorization result:', allowed)

# 11. Mind-Bending Questions
questions = [
    'What happens when roles has fewer items than users?',
    'What happens when two users have the same role?',
    'Why is a dictionary better than repeatedly scanning two lists?',
    'How would you represent a user with multiple roles?',
    'Does this mapping alone separate Tenant A from Tenant B?',
]
for number, question in enumerate(questions, 1):
    print(f'Q{number}: {question}')

# Answers
print('Answers: zip truncates; duplicate values are fine; dictionary lookup is direct; use a list or set of roles; add tenant identity.')

# 12. Interview Connection
print('Interview: hash-table lookup, zip truncation, dictionary uniqueness, and space complexity.')

# 13. Common Mistakes
# WRONG: mapping = {users: roles}  # lists are not hashable keys.
# CORRECT: mapping = dict(zip(users, roles))
# WRONG: roles[users.index('sam')]  # repeated list searches.
# CORRECT: mapping['sam']

# 14. Small Extension
# Add multiple roles per user, then add an action -> allowed-role mapping.

# 15. Connection Graph
# zip -> pair data -> dictionary mapping -> API authorization -> tenant permissions -> LLM tool access
