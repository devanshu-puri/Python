"""Module 7 - Treat functions as data in a small processing pipeline."""

# 1. Real-World Scenario
# A report can apply different scoring rules without rewriting the pipeline.

# 2. The Challenge
scores = [40, 65, 90]
# Build a function that accepts another function and applies it to every score.

# 3. My Current Python Toolkit
# Functions are objects; a list can store them; a loop can call each one.

# 4. Think Before Coding
# What input/output contract should each rule follow? Who chooses the rule?

# 5. Try It Yourself
# Create apply_rule(values, rule) and test it with a bonus rule.

# 6. Solution

def apply_rule_a(values, rule):
    result = []
    for value in values:
        result.append(rule(value))
    return result


def bonus(score):
    return score + 5

print('Version A:', apply_rule_a(scores, bonus))

apply_rule_b = lambda values, rule: [rule(value) for value in values]
print('Version B:', apply_rule_b(scores, lambda score: score * 2))
# A named function is clearer for reusable logic; a lambda is fine for a tiny one-off rule.

# 7. Trace It Visually
# [40, 65, 90] -> bonus(40), bonus(65), bonus(90) -> [45, 70, 95].

# 8. What Is Actually Happening Internally?
# The caller passes a function reference. The processing function calls it with one value.

# 9. THE IMPORTANT PART - THIS BECOMES...
# Python: function as a value
# Backend: configurable validation or transformation
# Production: pipeline stages and callbacks
# AI / LLM: model/provider strategy chosen at runtime
# Advanced System: plugin or agent tool registry [LEARN LATER]

# 10. Future Code Example

def run_model(text, model_function):
    return {'text': text, 'answer': model_function(text)}

print('Model strategy:', run_model('hello', lambda text: text.upper()))

# 11. Mind-Bending Questions
questions = [
    'What does it mean to pass a function as an argument?',
    'Why should all rules return a compatible type?',
    'When is a lambda less readable than def?',
    'How could you select a model function from a dictionary?',
    'What security check is needed before loading external functions?',
]
for number, question in enumerate(questions, 1):
    print(f'Q{number}: {question}')

# Answers
print('Answers: a function is an object reference; consistent output keeps pipelines composable; use def for named logic; map names to functions; validate allowed tools.')

# 12. Interview Connection
print('Interview: first-class functions, higher-order functions, callbacks, and strategy design.')

# 13. Common Mistakes
# WRONG: apply_rule_b(scores, bonus())  # calls bonus immediately with no argument.
# CORRECT: apply_rule_b(scores, bonus)
# WRONG: rules = [bonus()]  # stores a result, not a function.
# CORRECT: rules = [bonus]

# 14. Small Extension
# Add a validation rule, a logging wrapper, and a dictionary of named strategies.

# 15. Connection Graph
# function object -> callback -> configurable pipeline -> model strategy -> agent tool registry
