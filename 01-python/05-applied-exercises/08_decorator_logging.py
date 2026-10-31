"""Module 8 - Add logging around a function with a decorator."""

from functools import wraps

# 1. Real-World Scenario
# A service needs to record which operations run without editing each operation.

# 2. The Challenge
# Write a decorator that prints a start and finish message around a function.

# 3. My Current Python Toolkit
# Functions can wrap functions; *args/**kwargs forward any arguments; try/finally handles completion.

# 4. Think Before Coding
# What if the wrapped function accepts arguments? What if it raises an error?

# 5. Try It Yourself
# Build log_calls before reading the solution.

# 6. Solution

def log_calls(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print('START', function.__name__)
        try:
            return function(*args, **kwargs)
        finally:
            print('END', function.__name__)
    return wrapper


@log_calls
def add(first, second):
    return first + second

print('Version A/B:', add(2, 3))
# The decorator removes repeated logging code from each business function.

# 7. Trace It Visually
# add(2, 3) -> wrapper -> START -> original add -> result 5 -> END -> caller.

# 8. What Is Actually Happening Internally?
# @log_calls replaces add with wrapper. wraps preserves useful metadata such as __name__.

# 9. THE IMPORTANT PART - THIS BECOMES...
# Python: wrapper function
# Backend: logging, timing, authentication, and error boundaries
# Production: consistent observability across services
# AI / LLM: trace retrieval, prompt, model, and tool calls
# Advanced System: distributed tracing and correlation IDs [LEARN LATER]

# 10. Future Code Example
@log_calls
def retrieve_documents(query):
    return [f'document for {query}']

print('Retrieved:', retrieve_documents('Python'))

# 11. Mind-Bending Questions
questions = [
    'Why must wrapper accept *args and **kwargs?',
    'Why does finally run when the wrapped function raises?',
    'What problem does wraps solve?',
    'How could a decorator measure duration?',
    'Why should logs include a request ID in a real system?',
]
for number, question in enumerate(questions, 1):
    print(f'Q{number}: {question}')

# Answers
print('Answers: flexible forwarding; finally runs during cleanup; wraps preserves metadata; record start/end times; IDs connect logs across calls.')

# 12. Interview Connection
print('Interview: closures, decorators, exception propagation, metadata, and cross-cutting concerns.')

# 13. Common Mistakes
# WRONG: def wrapper(): return function()  # loses caller arguments.
# CORRECT: def wrapper(*args, **kwargs): return function(*args, **kwargs)
# WRONG: swallowing every exception in the decorator.
# CORRECT: log it if needed, then let the caller handle the error unless policy says otherwise.

# 14. Small Extension
# Add timing, a retry decorator, or a decorator that requires a permission.

# 15. Connection Graph
# function -> wrapper -> logging -> API observability -> tracing -> AI pipeline monitoring
