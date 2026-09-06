"""Module 2 - Use sets to check permissions."""

# 1. Real-World Scenario
# A user has permissions and an endpoint requires a small set of permissions.

# 2. The Challenge
user_permissions = {'read', 'write', 'export'}
required_permissions = {'read', 'export'}
# Decide whether access should be allowed.

# 3. My Current Python Toolkit
# Sets remove duplicates and make membership checks natural; subset checks compare groups.

# 4. Think Before Coding
# Should the user need every permission or only one? What happens with duplicates?

# 5. Try It Yourself
# Write the access check before looking below.

# 6. Solution
allowed_a = True
for permission in required_permissions:
    if permission not in user_permissions:
        allowed_a = False
        break
print('Version A:', allowed_a)

allowed_b = required_permissions <= user_permissions
print('Version B:', allowed_b)
print('shared permissions:', user_permissions & required_permissions)
print('extra permissions:', user_permissions - required_permissions)
# The subset expression is compact; the loop is useful when you need a reason for denial.

# 7. Trace It Visually
# required {read, export} <= user {read, write, export} -> True.
# missing {delete} -> {delete} is not a subset -> False.

# 8. What Is Actually Happening Internally?
# Set membership is designed for fast existence checks. A set stores unique values.

# 9. THE IMPORTANT PART - THIS BECOMES...
# Python: permission membership
# Backend: route authorization
# Production: roles expand into permission sets and audit decisions
# AI / LLM: tool permission checks before a model action
# Advanced System: tenant-aware policy evaluation [LEARN LATER]

# 10. Future Code Example
requested_tool = 'send_email'
tool_permissions = {'search_docs', 'send_email'}
print('Tool allowed:', requested_tool in tool_permissions)

# 11. Mind-Bending Questions
questions = [
    'Why is a set better than a list for repeated membership checks?',
    'What does required_permissions <= user_permissions mean?',
    'What information is lost when converting a list to a set?',
    'How would you report missing permissions?',
    'Can this check prevent cross-tenant access by itself?',
]
for number, question in enumerate(questions, 1):
    print(f'Q{number}: {question}')

# Answers
print('Answers: sets fit membership; <= means subset; order and duplicates are lost; use required - user; tenant identity is also required.')

# 12. Interview Connection
print('Interview: hash sets, average membership complexity, subset/intersection, and authorization modeling.')

# 13. Common Mistakes
# WRONG: if user_permissions == required_permissions:  # rejects harmless extra permissions.
# CORRECT: if required_permissions <= user_permissions:
# WRONG: required_permissions.issubset(user_permissions) is not the same as equality.
# CORRECT: choose subset or equality based on the policy.

# 14. Small Extension
# Add roles, deny rules, and a function that returns missing permissions.

# 15. Connection Graph
# set -> membership -> permission check -> API authorization -> policy engine -> secure tool use
