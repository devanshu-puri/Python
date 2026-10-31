"""
Python chapter: handling exceptions (runtime errors)

Run: python TryExcept.py

Basic sequence:
    try      -> run code that might fail
    except   -> handle a matching error
    else     -> run only if try had no error
    finally  -> run either way (usually cleanup)

Use the parts you need; try/except alone is valid.
"""


# 1. Handle one expected error with a specific except
try:
    number = int("not a number")
except ValueError as error:
    print("Conversion failed:", error)
# Conversion failed: ...


# 2. Different errors can have different responses
def divide_text(numerator_text, denominator_text):
    try:
        numerator = float(numerator_text)
        denominator = float(denominator_text)
        result = numerator / denominator
    except ValueError:
        print("Enter numbers, such as '12' and '3'.")
    except ZeroDivisionError:
        print("The denominator cannot be zero.")
    else:
        print("Result:", result)


divide_text("12", "3")       # Result: 4.0
divide_text("twelve", "3")   # Enter numbers...
divide_text("12", "0")       # The denominator cannot be zero.


# 3. The else block runs only when try succeeds
try:
    age = int("21")
except ValueError:
    print("Age must be a whole number.")
else:
    print("Next year:", age + 1)


# 4. finally runs whether an error happened or not
try:
    print("Trying a calculation...")
    answer = 8 / 2
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("Calculation attempt finished.")

# finally is useful for cleanup. For files, prefer `with` below: it closes
# the file automatically, even if reading raises an exception.


# 5. File case: open -> read -> handle a missing file
def show_file(path):
    try:
        with open(path, encoding="utf-8") as file:
            contents = file.read()
    except FileNotFoundError:
        print(f"File not found: {path}")
    except PermissionError:
        print(f"No permission to read: {path}")
    else:
        print(contents)


# This is safe to run even when the example file does not exist:
show_file("intermediate/text.txt")


# 6. Raise an error when the input is invalid
def positive_area(width, height):
    if width <= 0 or height <= 0:
        raise ValueError("width and height must be positive")
    return width * height


print("Area:", positive_area(4, 5))
# positive_area(0, 5) raises ValueError; callers can catch it if appropriate.


# 7. Common mistakes and Pythonic habits
#
# Avoid:
#   except:                  # catches almost everything, including interrupts
#       pass                 # silently hides the problem
#
# Prefer:
#   except ValueError as error:
#       print(error)         # or handle/log it meaningfully
#
# Also remember:
#   * Put more specific except clauses before broader exception classes.
#   * The try block should contain only the code that may raise the errors
#     you intend to handle.
#   * `else` keeps success-only code out of the try block.
#   * Do not catch an error just to print it and continue as if the work worked.
#   * `raise` reports an invalid situation; it does not fix it.
#   * `with open(...)` handles file closing. `finally` remains useful for other
#     cleanup that has no context manager.


# FUTURE GLIMPSE
# Backend / FastAPI: turn expected errors into clear API responses.
# Databases: handle a failed query or missing record intentionally.
# Data / AI / RAG: malformed input or unavailable files may need handling.
# Async / distributed systems: [LEARN LATER] timeouts and network errors need
# their own deliberate handling; a broad except is not a safe retry strategy.


# INTERVIEW QUESTIONS — try before reading the answers
#
# Easy
# 1. Which block runs only if no exception occurs: except, else, or finally?
# 2. What error does int("abc") raise?
#
# Medium
# 3. What happens if no except clause matches the raised error?
# 4. In the file example, why use `with open(...)` rather than manual close?
# 5. What is printed by divide_text("8", "0")?
#
# Tricky
# 6. Why should `except ValueError` usually come before `except Exception`?
# 7. Does finally run when the try block returns a value?
# 8. What is wrong with `except Exception: pass`?
#
# ANSWERS + EXPLANATIONS
# 1. else. It runs after a successful try block.
# 2. ValueError. The text is not a valid integer representation.
# 3. The exception continues outward to the caller; if nobody handles it,
#    Python displays a traceback and stops that operation.
# 4. `with` closes the file automatically, including when an error occurs.
# 5. "The denominator cannot be zero."
# 6. ValueError is specific. A broad earlier handler would catch it first and
#    prevent the later specific handler from running.
# 7. Yes. finally runs before the function actually returns.
# 8. It swallows every Exception and hides the cause, making bugs difficult to
#    find and potentially letting broken work appear successful.


# MINI PRACTICE — implement without copying an answer
# 1. Easy: Convert a string to int; print a friendly message for ValueError.
# 2. Easy/Medium: Write safe_divide(a, b) that catches only division by zero.
# 3. Medium: Validate a person's age; raise ValueError if it is negative.
# 4. Tricky: Read a file using `with`, handling missing file and permission
#    errors separately.
# 5. Interview-style: Write a function that converts input to float, returns
#    the number when valid, and raises a clear ValueError otherwise.


# ROADMAP
# Exceptions -> detect and handle failures -> API, database, and file errors
#             -> reliable backend and AI/data pipelines
#
# FINAL CHECKLIST
# MUST KNOW: try/except, specific errors, raise.
# GOOD TO KNOW: else, finally, with.
# LEARN LATER: async/network error policies and retries.
# BACKEND: meaningful handling of request and service failures.
# AI ENGINEERING: handle invalid data and failed model/service calls.
# INTERVIEW: exception order; else vs finally; why not to swallow errors.
