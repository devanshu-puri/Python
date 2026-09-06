"""Module 4 - Transform API-style records into a frontend shape."""

# 1. Real-World Scenario
# An upstream API returns verbose user records, but our client needs a smaller response.

# 2. The Challenge
api_users = [
    {'id': 1, 'first_name': 'Ava', 'last_name': 'Stone', 'email': 'ava@example.com'},
    {'id': 2, 'first_name': 'Sam', 'last_name': 'Lee', 'email': 'sam@example.com'},
]
# Create records with id, display_name, and email.

# 3. My Current Python Toolkit
# Dictionaries model records; functions isolate transformation rules; comprehensions map lists.

# 4. Think Before Coding
# Which fields are public? What happens if a field is missing? Should the original records change?

# 5. Try It Yourself
# Build a new list without mutating api_users.

# 6. Solution

def transform_user(user):
    return {
        'id': user['id'],
        'display_name': f"{user['first_name']} {user['last_name']}",
        'email': user['email'],
    }

transformed_a = []
for user in api_users:
    transformed_a.append(transform_user(user))
print('Version A:', transformed_a)

transformed_b = [transform_user(user) for user in api_users]
print('Version B:', transformed_b)
# A named function keeps the mapping rule testable; the comprehension keeps the batch concise.

# 7. Trace It Visually
# verbose record -> transform_user() -> smaller public record.
# list of two records -> list of two transformed records.

# 8. What Is Actually Happening Internally?
# Each input dictionary is read and a new dictionary is returned. The source list is unchanged.

# 9. THE IMPORTANT PART - THIS BECOMES...
# Python: map fields from one dictionary shape to another
# Backend: API response serializer
# Production: schema validation, versioning, and privacy filtering
# AI / LLM: convert model/provider responses into one internal shape
# Advanced System: stable contracts between services [LEARN LATER]

# 10. Future Code Example
provider_response = {'output_text': 'Answer', 'usage': {'tokens': 42}}
internal_response = {
    'answer': provider_response['output_text'],
    'tokens_used': provider_response['usage']['tokens'],
}
print('Internal response:', internal_response)

# 11. Mind-Bending Questions
questions = [
    'Why create new dictionaries instead of changing the API data?',
    'What happens when first_name is missing?',
    'How would you hide email from the response?',
    'Where should a transformation happen for a huge database result?',
    'Why is one internal response shape useful with multiple providers?',
]
for number, question in enumerate(questions, 1):
    print(f'Q{number}: {question}')

# Answers
print('Answers: preserve source data; missing keys raise KeyError; omit email; transform in batches or at the query boundary; stable shape isolates provider differences.')

# 12. Interview Connection
print('Interview: data modeling, pure functions, copying, schema boundaries, and API contracts.')

# 13. Common Mistakes
# WRONG: user['display_name'] = ...  # mutates an upstream record.
# CORRECT: return a new dictionary.
# WRONG: transformed = list(map(transform_user, api_users)) without understanding transform_user.
# CORRECT: learn the loop first, then use map or comprehension when it stays readable.

# 14. Small Extension
# Add an optional phone field, remove private fields, and support an API version field.

# 15. Connection Graph
# dict -> transform function -> response shape -> API contract -> provider adapter -> LLM gateway
