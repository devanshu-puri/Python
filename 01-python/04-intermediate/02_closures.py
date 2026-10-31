"""
Closure chapter (short mentor version)
1. MUST KNOW
- A closure is a function that remembers variables from its outer scope.
- The outer function usually returns the inner function, not the result of calling it.
- This is useful for callbacks, decorators, and factory functions.
2. SKIPPED OFTEN
- lexical scoping
- free variables
- nonlocal keyword
3. COMMON MISTAKES
- return inner_func() instead of return inner_func
- calling outer_func() without arguments
4. USED LATER
- Backend: decorators, route logic, request/session handling
- AI: callbacks, wrappers, cached behaviors, prompts
- APIs/FastAPI: dependency functions, custom logic wrappers
5. INTERVIEW TRAPS
- return value is None if you call inner function too early
- Python stores references, not copies
"""

# 1) Basic closure

def outer_func(msg):
    message = msg

    def inner_func():
        print(message)

    return inner_func

hi_func = outer_func("HI")
hello_func = outer_func("Hello")
hi_func()
hello_func()

# 2) Common mistake: returning inner_func() instead of inner_func

def bad_outer(msg):
    message = msg

    def inner():
        print(message)

    return inner()  # WRONG for closure factory pattern

# bad_outer("Oops")  # returns None, then bad_outer(...)() would fail

# 3) Using nonlocal to modify outer variable

def counter():
    count = 0

    def inc():
        nonlocal count
        count += 1
        return count

    return inc

c = counter()
print(c())
print(c())
print(c())

# 4) Closure with a list (mutable outer value)

def make_builder(prefix):
    items = []

    def add(x):
        items.append(prefix + str(x))
        return items

    return add

add_a = make_builder("A-")
add_b = make_builder("B-")
print(add_a(1))
print(add_a(2))
print(add_b(1))

# 5) Quick questions for you:
# Q1: Why does outer_func("HI") return a function instead of printing immediately?
# Q2: What is the difference between return inner_func and return inner_func()?
# Q3: Why does nonlocal count work but count = count + 1 would fail without it?
# Q4: Why is this useful for decorators and API wrappers later?
# Q5: What happens if you call outer_func() with no arguments?

# MINI PRACTICE
# 1) Write a function that returns a function which multiplies by 10.
# 2) Write a closure that stores a username and prints it when called.
# 3) Explain why a variable from outer scope can still be used after the outer function ends.

# FUTURE ROADMAP
# Closure -> function factories + decorators -> FastAPI dependencies + custom wrappers -> AI task runners

   