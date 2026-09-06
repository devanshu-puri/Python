"""Module 9 - Process large data with a generator."""

# 1. Real-World Scenario
# A log file contains many lines. We want error lines without loading everything.

# 2. The Challenge
# Produce matching lines one at a time.

# 3. My Current Python Toolkit
# Iteration visits values; yield pauses a function and produces the next value later.

# 4. Think Before Coding
# When should work happen? How is memory different from a list?

# 5. Try It Yourself
# Write error_lines(lines) using yield.

# 6. Solution

def error_lines(lines):
    for line in lines:
        if 'ERROR' in line:
            yield line


log_lines = ['INFO started', 'ERROR database', 'INFO finished', 'ERROR timeout']
print('Version A:', list(error_lines(log_lines)))

# The list version creates all matching results immediately.
errors_b = [line for line in log_lines if 'ERROR' in line]
print('Version B:', errors_b)
# A generator is better for a large or streaming input; a list is easier when data is small and reused.

# 7. Trace It Visually
# call generator -> pause before first line -> next() -> matching line -> next() -> next match.

# 8. What Is Actually Happening Internally?
# Calling error_lines returns a generator object. Its body runs as next() requests values.

# 9. THE IMPORTANT PART - THIS BECOMES...
# Python: lazy iteration
# Backend: stream rows or upload chunks
# Production: bounded memory data processing
# AI / LLM: stream documents or model output
# Advanced System: queue and worker pipelines [LEARN LATER]

# 10. Future Code Example

def chunk_text(words, size):
    for start in range(0, len(words), size):
        yield words[start:start + size]

print('Text chunks:', list(chunk_text(['a', 'b', 'c', 'd', 'e'], 2)))

# 11. Mind-Bending Questions
questions = [
    'When does a generator body execute?',
    'What happens after it is exhausted?',
    'Why can a generator reduce memory use?',
    'Why can you not freely index every generator?',
    'What backpressure problem can streaming help with?',
]
for number, question in enumerate(questions, 1):
    print(f'Q{number}: {question}')

# Answers
print('Answers: on next(); StopIteration after exhaustion; values are produced one at a time; generators are not usually random-access; consumers can process at their pace.')

# 12. Interview Connection
print('Interview: iterators, lazy evaluation, StopIteration, memory complexity, and one-pass data.')

# 13. Common Mistakes
# WRONG: print(error_lines(log_lines))  # prints a generator object, not its values.
# CORRECT: for line in error_lines(log_lines): print(line)
# WRONG: use the same exhausted generator twice.
# CORRECT: create a new generator when another pass is needed.

# 14. Small Extension
# Read a real file line by line, batch chunks, and stop after a maximum number of errors.

# 15. Connection Graph
# yield -> lazy iteration -> streaming -> bounded-memory service -> document streaming/RAG ingestion
