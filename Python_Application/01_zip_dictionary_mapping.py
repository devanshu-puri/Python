
"""Module 1 - Pair users with roles using zip and a dictionary."""

# 1. REAL-WORLD SCENARIO
# An access-control service receives two lists:
# - users: usernames
# - roles: the role assigned to each username at the same index
#
# For example:
# users[0] = 'ava' corresponds to roles[0] = 'admin'.


# 2. THE CHALLENGE
users = ['ava', 'sam', 'mia']
roles = ['admin', 'editor', 'viewer']

# Task A:
# Create a dictionary named user_to_role that maps each
# username to its corresponding role.
#
# Expected dictionary:
# {
#     'ava': 'admin',
#     'sam': 'editor',
#     'mia': 'viewer'
# }
#
# Task B:
# Create a list named editors containing all users whose
# role allows them to edit content.
#
# RULE: Both 'admin' and 'editor' roles can edit.
#
# Expected list:
# ['ava', 'sam']


# 3. MY CURRENT PYTHON TOOLKIT
# Use these concepts:
# - zip(users, roles): pairs usernames with their roles.
# - dict(...): creates a dictionary from key-value pairs.
# - .items(): iterates over dictionary keys and values.
# - List comprehension: filters users based on their roles.


# 4. THINK BEFORE CODING

# Q1. What happens if the lists have different lengths?
#
# Consider this specific input:
# users = ['ava', 'sam', 'mia']
# roles = ['admin', 'editor']
#
# TASK: Predict the result of dict(zip(users, roles)).
# Assume zip() uses its default behavior.
#
# Q2. What should duplicate roles mean?
#
# Consider this specific input:
# users = ['ava', 'sam']
# roles = ['editor', 'editor']
#
# TASK: Explain whether both users can have the same role.
#
# Also consider:
# users = ['ava', 'ava']
# roles = ['admin', 'viewer']
#
# TASK: Predict what dict(zip(users, roles)) produces.
# Explain why the result occurs.
#
# ASSUMPTIONS FOR THIS MODULE:
# - Every user should have exactly one role.
# - Duplicate role values are allowed.
# - Duplicate usernames are invalid input and should be
#   detected in a production implementation.
# - The main exercise uses equal-length lists with unique users.


# 5. TRY IT YOURSELF
# Complete these tasks BEFORE looking at Section 6.
#
# TODO 2: Find users whose role is 'admin' or 'editor'.
# TODO 3: Build the same dictionary using dict(zip(...)).
# TODO 4: Print the dictionary and the list of allowed users.


# 6. SOLUTION

# Version A - Build the dictionary using a loop.
user_to_role_a = {}

for user, role in zip(users, roles):
    user_to_role_a[user] = role

editors_a = [
    user
    for user, role in user_to_role_a.items()
    if role in {'admin', 'editor'}
]

print('Version A:', user_to_role_a, editors_a)


# Version B - Build the dictionary using dict() and zip().
user_to_role_b = dict(zip(users, roles))

editors_b = [
    user
    for user, role in user_to_role_b.items()
    if role in {'admin', 'editor'}
]

print('Version B:', user_to_role_b, editors_b)

# Version B is more concise.
# Version A is useful when validation or extra processing is needed.


# 7. TRACE IT VISUALLY

# Initial dictionary:
# {}
#
# Pair 1: ('ava', 'admin')
# Dictionary: {'ava': 'admin'}
# Ava is allowed to edit.
#
# Pair 2: ('sam', 'editor')
# Dictionary: {'ava': 'admin', 'sam': 'editor'}
# Sam is allowed to edit.
#
# Pair 3: ('mia', 'viewer')
# Dictionary:
# {'ava': 'admin', 'sam': 'editor', 'mia': 'viewer'}
# Mia is not allowed to edit.
#
# Final editors list: ['ava', 'sam']


# 8. WHAT IS ACTUALLY HAPPENING INTERNALLY?

# Q1: What does zip() produce from two lists?
# Q2: Does zip() produce pairs lazily?
# Q3: What happens when the input lengths differ?
# Q4: How does dict() consume the pairs?
#
# Key facts:
# - zip() pairs elements at corresponding positions.
# - zip() produces pairs lazily.
# - By default, zip() stops at the shortest input.
# - dict() consumes the pairs to build a mapping.


# 9. THE IMPORTANT PART - THIS BECOMES...

# Python:
# username -> role mapping
#
# Backend:
# Look up a user's role when processing an API request.
#
# Production:
# tenant_id + user_id -> permissions
#
# AI / LLM:
# Restrict which tools or documents a user can access.
#
# Advanced system:
# Multi-tenant access control [LEARN LATER]


# 10. FUTURE CODE EXAMPLE - AUTHORIZATION CHECK

request = {'user': 'sam', 'action': 'edit'}

allowed = (
    request['action'] in {'view', 'edit'}
    and user_to_role_b[request['user']] != 'viewer'
)

print('Future authorization result:', allowed)

# This is a simplified example, not production-ready authorization.
# A real system must check the specific action, handle unknown users,
# and enforce permissions within the correct tenant.
#
# Note: This example assumes every non-viewer role can perform
# both 'view' and 'edit'. Production permissions should be explicit.


# 11. MIND-BENDING QUESTIONS

# Q1. What happens when roles has fewer items than users?
#     Use the example in Section 4 to determine the result.
#
# Q2. What happens when two users have the same role?
#     Use the example in Section 4 to explain the behavior.
#
# Q3. Why is a dictionary better than repeatedly scanning two lists?
#     Compare looking up a user's role in a dictionary with
#     finding the user's index in a list and accessing the role
#     at the same index.
#
# Q4. How would you represent a user with multiple roles?
#     Assume Ava can be both an admin and a viewer.
#     Write the dictionary entry that represents this.
#
# Q5. Does this mapping alone separate Tenant A from Tenant B?
#     Assume both tenants can have a user named 'sam'.
#     Explain why a username-only mapping cannot distinguish them.


# 12. INTERVIEW CONNECTION

# Be prepared to explain:
# - Hash-table lookup.
# - zip() truncation.
# - Dictionary key uniqueness versus duplicate values.
# - Time and space complexity.
#
# Practice question:
# Why does a dictionary generally provide faster repeated
# key-based lookups than repeatedly scanning a list?


# 13. COMMON MISTAKES

# WRONG:
# mapping = {users: roles}
#
# Why?
# Lists are mutable and unhashable, so they cannot be dictionary keys.
#
# CORRECT:
mapping = dict(zip(users, roles))

# LESS EFFICIENT FOR REPEATED LOOKUPS:
# roles[users.index('sam')]
#
# PREFERRED WHEN THE MAPPING ALREADY EXISTS:
print("Sam's role:", mapping['sam'])


# 14. SMALL EXTENSION

# Extension A:
# Modify the mapping so each user can have multiple roles.
#
# Example input:
# users = ['ava', 'sam', 'ava', 'mia', 'sam']
# roles = ['admin', 'editor', 'viewer', 'editor', 'viewer']
#
# Expected mapping:
# {
#     'ava': ['admin', 'viewer'],
#     'sam': ['editor', 'viewer'],
#     'mia': ['editor']
# }
#
# Extension B:
# Create an action -> allowed roles mapping.
#
# Example requirements:
# - 'view' is allowed for 'admin', 'editor', and 'viewer'.
# - 'edit' is allowed for 'admin' and 'editor'.
#
# Use the mapping to determine whether a user's role
# permits a requested action.


# 15. CONNECTION GRAPH

# zip()
#   -> pair related data
#   -> build a dictionary mapping
#   -> perform API authorization lookups
#   -> manage tenant permissions
#   -> control LLM tool and document access
