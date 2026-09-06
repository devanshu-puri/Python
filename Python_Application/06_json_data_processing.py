"""Module 6 - Parse JSON data and build a useful report."""

import json

# 1. Real-World Scenario
# A webhook sends JSON text containing events. We need valid payment events.

# 2. The Challenge
json_text = '''
[
    {"id": 1, "type": "payment", "status": "success"},
    {"id": 2, "type": "login", "status": "success"},
    {"id": 3, "type": "payment", "status": "failed"}
]
'''
# Parse the text and select successful payments.

# 3. My Current Python Toolkit
# json.loads creates Python lists/dictionaries; loops and conditions inspect records.

# 4. Think Before Coding
# What happens if the JSON is malformed? Which fields are required?

# 5. Try It Yourself
# Parse json_text and build a list of successful payment IDs.

# 6. Solution

events = json.loads(json_text)
successful_a = []
for event in events:
    if event.get('type') == 'payment' and event.get('status') == 'success':
        successful_a.append(event['id'])
print('Version A:', successful_a)

successful_b = [
    event['id'] for event in events
    if event.get('type') == 'payment' and event.get('status') == 'success'
]
print('Version B:', successful_b)

# json.dumps converts Python data back to JSON text.
report = {'successful_payment_ids': successful_b, 'count': len(successful_b)}
print('JSON report:', json.dumps(report))
# Comprehension is compact; the loop is better when validation and logging are needed.

# 7. Trace It Visually
# JSON text -> loads() -> list of dictionaries -> filter -> [1] -> dumps() -> JSON text.

# 8. What Is Actually Happening Internally?
# JSON has text syntax. loads parses it into Python objects; dumps serializes Python objects.

# 9. THE IMPORTANT PART - THIS BECOMES...
# Python: parse -> inspect -> transform -> serialize
# Backend: webhook or API request handling
# Production: schema validation, retries, idempotency, and logging
# AI / LLM: parse structured model output into application data
# Advanced System: event pipeline processing [LEARN LATER]

# 10. Future Code Example

def parse_model_result(text):
    try:
        result = json.loads(text)
    except json.JSONDecodeError:
        return {'ok': False, 'error': 'invalid JSON'}
    return {'ok': True, 'answer': result.get('answer', '')}

print('Model result:', parse_model_result('{"answer": "ready"}'))

# 11. Mind-Bending Questions
questions = [
    'What is the difference between JSON text and a Python dictionary?',
    'What exception does malformed JSON raise?',
    'Why use get() for optional fields?',
    'How would you prevent processing the same event twice?',
    'Why should model output be validated before use?',
]
for number, question in enumerate(questions, 1):
    print(f'Q{number}: {question}')

# Answers
print('Answers: JSON is text; JSONDecodeError signals bad syntax; get avoids missing-key failure; store event IDs; untrusted output needs validation.')

# 12. Interview Connection
print('Interview: serialization, parsing errors, schema validation, idempotency, and data boundaries.')

# 13. Common Mistakes
# WRONG: json.loads(report) when report is already a dictionary.
# CORRECT: call loads for text and use the dictionary directly.
# WRONG: data = json.loads(bytes_data) without understanding the input type.
# CORRECT: decode bytes when necessary, then parse text.

# 14. Small Extension
# Add malformed-input handling, event type counts, and a processed-event ID set.

# 15. Connection Graph
# JSON text -> Python records -> filtering -> API/webhook handling -> event processing -> structured LLM output
