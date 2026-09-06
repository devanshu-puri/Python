"""Module 5 - Group records by role."""

# 1. Real-World Scenario
# An admin report needs users grouped under each role.

# 2. The Challenge
users = [
    {'name': 'Ava', 'role': 'admin'},
    {'name': 'Sam', 'role': 'editor'},
    {'name': 'Mia', 'role': 'editor'},
]
# Build {'admin': ['Ava'], 'editor': ['Sam', 'Mia']}.

# 3. My Current Python Toolkit
# A dictionary can hold a list per key. setdefault creates a bucket when needed.

# 4. Think Before Coding
# What happens on the first user for a role? What if a user has multiple roles?

# 5. Try It Yourself
# Group names by role without sorting the input first.

# 6. Solution

grouped_a = {}
for user in users:
    role = user['role']
    if role not in grouped_a:
        grouped_a[role] = []
    grouped_a[role].append(user['name'])
print('Version A:', grouped_a)

grouped_b = {}
for user in users:
    grouped_b.setdefault(user['role'], []).append(user['name'])
print('Version B:', grouped_b)
# The explicit version is easier to debug; setdefault is concise for a known simple pattern.

# 7. Trace It Visually
# admin -> create [] -> append Ava.
# editor -> create [] -> append Sam -> append Mia.

# 8. What Is Actually Happening Internally?
# The role is the dictionary key and its value is a mutable list that accumulates names.

# 9. THE IMPORTANT PART - THIS BECOMES...
# Python: key -> collection grouping
# Backend: group orders by status or users by organization
# Production: database GROUP BY and aggregation
# AI / LLM: group retrieved chunks by source or document
# Advanced System: partition work by tenant or queue [LEARN LATER]

# 10. Future Code Example
chunks = [
    {'source': 'guide.md', 'text': 'one'},
    {'source': 'guide.md', 'text': 'two'},
    {'source': 'faq.md', 'text': 'three'},
]
by_source = {}
for chunk in chunks:
    by_source.setdefault(chunk['source'], []).append(chunk['text'])
print('Chunks by source:', by_source)

# 11. Mind-Bending Questions
questions = [
    'Why must the value be a list?',
    'What happens if role is missing?',
    'How would you count each group instead of storing names?',
    'When would a database perform this grouping better?',
    'What key would keep tenants from being mixed?',
]
for number, question in enumerate(questions, 1):
    print(f'Q{number}: {question}')

# Answers
print('Answers: one key may have many values; missing keys need validation; use counters; databases handle large aggregation; include tenant_id in the key.')

# 12. Interview Connection
print('Interview: nested mutable values, dictionary insertion, aggregation, and grouping complexity.')

# 13. Common Mistakes
# WRONG: grouped[role].append(name)  # fails before the first bucket exists.
# CORRECT: grouped.setdefault(role, []).append(name)
# WRONG: grouped = {user['role']: user['name'] for user in users}  # later users overwrite earlier ones.
# CORRECT: store a list when keys repeat.

# 14. Small Extension
# Group by (tenant_id, role), then compute counts and totals per group.

# 15. Connection Graph
# dictionary + list -> grouping -> report/API aggregation -> database GROUP BY -> chunk/source organization
