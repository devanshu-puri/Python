"""
Python chapter: decorators with arguments

Run this file with Python to see the examples:
    python DecoratorWithArgument.py

A decorator with arguments is a function that configures a decorator.
The extra function call is what makes it different from a plain decorator.
"""


# ---------------------------------------------------------------------------
# 1. The shape of a decorator with arguments
# ---------------------------------------------------------------------------

# A plain decorator receives the function directly:
#
#     @plain_decorator
#     def work():
#         ...
#
#     # Roughly equivalent to:
#     work = plain_decorator(work)
#
# A decorator with arguments adds an outer "decorator factory":
#
#     @configured_decorator("INFO")
#     def work():
#         ...
#
#     # Roughly equivalent to:
#     work = configured_decorator("INFO")(work)
#
# The levels are:
#   1. configured_decorator("INFO") receives decorator configuration.
#   2. The returned decorate function receives the original function.
#   3. The returned wrapper runs when the decorated function is called.
#
# Chapter check — MUST KNOW:
#   * A decorator is a callable that receives and returns a callable.
#   * An argument-taking decorator is usually a factory that returns a
#     decorator; its common structure has three nested function levels.
#   * The factory configuration is captured and reused by a closure.
#   * The wrapper forwards the original call and usually returns its result.
#   * Decorators are applied when Python executes the decorated def statement.
#
# Often skipped, but important:
#   * The decorated function's name is rebound to the decorator's return value.
#   * Decorator configuration errors can happen at definition/import time.
#   * functools.wraps preserves important metadata, but does not change the
#     wrapper's actual argument handling.
#   * Stacked decorators compose, so their order can change behavior.
#   * A wrapper should let errors propagate unless it has a deliberate,
#     documented reason to handle them.
#
# Useful syntax and tools in this chapter:
#   @factory(config)  -> factory(config)(function)
#   *args, **kwargs   -> forward arbitrary positional and keyword arguments
#   functools.wraps  -> copy useful metadata from the wrapped function
#   __name__, __doc__ -> inspect a function's visible name and documentation
#   return           -> preserve the wrapped function's result


def announce(label):
    """Create a decorator that prints a label before calling a function."""

    def decorate(function):
        def wrapper(*args, **kwargs):
            print(f"{label}: calling {function.__name__}")
            return function(*args, **kwargs)

        return wrapper

    return decorate


@announce("REPORT")
def make_report(owner):
    return f"Report for {owner}"


print(make_report("Mina"))
# REPORT: calling make_report
# Report for Mina


# ---------------------------------------------------------------------------
# 2. Configuration is captured by a closure
# ---------------------------------------------------------------------------

# `label` is local to announce(), but decorate() and wrapper() can still use
# it later. This is a closure. You only need to recognize this pattern now:
# the decorator factory remembers its configuration for each decorated function.


def add_prefix(prefix):
    def decorate(function):
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            return f"{prefix}{result}"

        return wrapper

    return decorate


@add_prefix("[API] ")
def get_status(code):
    return f"status={code}"


print(get_status(200))
# [API] status=200


# Each use can have different configuration:
@add_prefix("[DB] ")
def get_database_status():
    return "connected"


print(get_database_status())
# [DB] connected


# ---------------------------------------------------------------------------
# 3. Forward arguments and preserve the wrapped function's return value
# ---------------------------------------------------------------------------

# Use *args and **kwargs when a wrapper should accept whatever arguments the
# original function accepts. Forward both, and return the result; otherwise
# keyword arguments or the original return value can be lost.


def repeat(times):
    if times < 1:
        raise ValueError("times must be at least 1")

    def decorate(function):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = function(*args, **kwargs)
            return result

        return wrapper

    return decorate


@repeat(3)
def save_record(record_id, *, source):
    print(f"Saved {record_id} from {source}")
    return record_id


saved_id = save_record(42, source="web")
print("Returned:", saved_id)
# Saved 42 from web
# Saved 42 from web
# Saved 42 from web
# Returned: 42


# IMPORTANT: the decorator argument (`3`) is not an argument to save_record().
# `times` is read when @repeat(3) is evaluated; record_id and source are passed
# later when save_record(42, source="web") is called.


# ---------------------------------------------------------------------------
# 4. Use functools.wraps to keep function metadata
# ---------------------------------------------------------------------------

# A wrapper is a new function. Without @wraps, its name and documentation
# replace the original function's metadata.

from functools import wraps


def logged(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"Starting {function.__name__}")
        return function(*args, **kwargs)

    return wrapper


@logged
def calculate_total(price, quantity=1):
    """Return the total price."""
    return price * quantity


print(calculate_total(12, quantity=3))
print(calculate_total.__name__)
print(calculate_total.__doc__)
# Starting calculate_total
# 36
# calculate_total
# Return the total price.

# Pythonic default: use functools.wraps in real decorators that wrap functions.
# It keeps useful metadata for help(), debugging, tests, and web frameworks.


# ---------------------------------------------------------------------------
# 5. Decorator arguments and function arguments are different
# ---------------------------------------------------------------------------

def require_role(role):
    def decorate(function):
        @wraps(function)
        def wrapper(user_role, *args, **kwargs):
            if user_role != role:
                raise PermissionError(f"{role} role required")
            return function(*args, **kwargs)

        return wrapper

    return decorate


@require_role("admin")
def delete_user(user_id):
    return f"Deleted user {user_id}"


print(delete_user("admin", 17))
# Deleted user 17

# Calling delete_user("guest", 17) raises PermissionError. Exceptions raised
# inside a wrapper normally propagate to the caller; do not hide them silently.
# Real authorization needs careful design; this tiny example only illustrates
# where a configured rule can be checked.


# ---------------------------------------------------------------------------
# 6. Stacking decorators
# ---------------------------------------------------------------------------

def surround(left, right):
    def decorate(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            return f"{left}{function(*args, **kwargs)}{right}"

        return wrapper

    return decorate


def uppercase(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs).upper()

    return wrapper


@surround("<", ">")
@uppercase
def greeting(name):
    return f"Hello, {name}"


print(greeting("Kai"))
# <HELLO, KAI>

# Stacking is applied from the bottom up:
# greeting = surround("<", ">")(uppercase(greeting))
# Reversing the decorator order can change the result.


# ---------------------------------------------------------------------------
# 7. Useful checks and common mistakes
# ---------------------------------------------------------------------------

# The decorated name refers to the wrapper (or whatever the decorator returns):
#
#     @add_prefix("x")
#     def item():
#         return "y"
#
#     # `item` now refers to the decorated callable, not the original function.
#
# Common mistakes:
#   * Returning decorate instead of calling it: @announce instead of
#     @announce("REPORT") uses a different calling convention.
#   * Forgetting to return wrapper from decorate().
#   * Forgetting to return the original function's result from wrapper().
#   * Calling function() without forwarding *args and **kwargs.
#   * Mixing up configuration arguments (factory call time) with call
#     arguments (wrapper runtime).
#   * Forgetting functools.wraps and then being surprised by wrapper metadata.
#   * Assuming a decorator runs only when the function is called. The factory
#     and decorator are applied when Python executes the def statement.
#
# repeat(0) is explicitly rejected above. Validate decorator configuration
# early when invalid values would otherwise cause surprising behavior.
#
# Pythonic habits:
#   * Use functools.wraps on wrappers.
#   * Keep a wrapper's job small and forward arguments/results explicitly.
#   * Validate decorator options near the factory call.
#   * Use a plain decorator when configuration is not needed; use a factory
#     only when arguments actually configure behavior.


# Interview traps for this chapter:
#   * @decorator and @decorator(...) are not interchangeable spellings.
#   * A missing return in wrapper often turns the decorated function's result
#     into None.
#   * wraps helps metadata, not runtime signature enforcement.
#   * In a stack, the bottom decorator is applied first; the top wrapper runs
#     first when the decorated function is called.
#   * The decorator factory is evaluated once per decorated def, not once per
#     call. State stored in a closure can therefore persist across calls.


# ---------------------------------------------------------------------------
# 8. Where this appears later (glimpse only)
# ---------------------------------------------------------------------------

# Backend / APIs / FastAPI:
#   Decorators can attach routes, dependencies, permissions, or instrumentation.
#   Frameworks often rely on preserved function metadata and signatures.
#
# Databases:
#   A wrapper may log or time a query helper. Transactions and database
#   connection lifetimes are separate topics to learn later.
#
# Data processing:
#   A wrapper can apply consistent validation or logging around a transform.
#
# AI / ML:
#   A wrapper may record timing or metadata around a model-call function.
#
# RAG / LLM applications:
#   A wrapper may consistently instrument retrieval or generation calls.
#
# Async / concurrent programming:
#   [LEARN LATER] An async function returns a coroutine, so an async-aware
#   decorator must use async/await correctly. Concurrency and shared state add
#   more rules than the synchronous examples here.
#
# Distributed systems:
#   [LEARN LATER] A retry decorator can be useful around remote calls, but it
#   must account for failures, timeouts, and duplicate side effects. Do not
#   treat the simple repeat() example as a safe retry implementation.
#
# *args/**kwargs, closures, and functools.wraps matter repeatedly in these areas.
# Typing decorators precisely with ParamSpec is useful later, but not needed here.


# ---------------------------------------------------------------------------
# 9. Interview questions — try these before reading the answers
# ---------------------------------------------------------------------------

# Easy
# 1. In @add_prefix("[X] "), which call happens when Python defines the
#    decorated function, and which call happens when the function is invoked?
# 2. What is printed by greeting("Kai")? Why does decorator order matter?
#
# Medium
# 3. What bug appears if wrapper calls function(*args, **kwargs) but does not
#    return its result?
# 4. Why does save_record(42, source="web") print three times but return 42?
# 5. What exception does repeat(0) raise, and when is it raised?
#
# Tricky
# 6. What does calculate_total.__name__ contain with @wraps, and what would it
#    usually contain without @wraps?
# 7. Explain the expansion of @announce("REPORT") on make_report.
# 8. If two decorators are stacked, which one is applied first?
# 9. Why can a wrapper accepting only `value` break a decorated function that
#    is called with a keyword argument or with multiple arguments?
#
# Small coding question
# 10. Write a decorator factory `times_called(limit)` that prints a message
#     before each call. (Do not implement a production call counter yet.)


# ---------------------------------------------------------------------------
# ANSWERS + EXPLANATIONS
# ---------------------------------------------------------------------------

# 1. add_prefix("[X] ") runs at definition time and returns a decorator.
#    The returned decorator receives the function. The wrapper runs on each
#    later invocation of that decorated function.
#
# 2. It prints <HELLO, KAI>. The bottom decorator is applied first; composition
#    order changes which value each wrapper receives and returns.
#
# 3. The decorated call evaluates to None, even if the original function
#    returned a useful value. A wrapper should usually return that result.
#
# 4. repeat(3) invokes the original three times. The wrapper stores each result
#    and returns the last one, which is 42.
#
# 5. ValueError, raised immediately while evaluating @repeat(0), before the
#    decorated function can be called.
#
# 6. It is "calculate_total". Without @wraps, the visible name is generally
#    "wrapper", because that is the function returned by logged().
#
# 7. Roughly: make_report = announce("REPORT")(make_report). The first call
#    creates a decorator; that decorator receives the original function.
#
# 8. The bottom decorator is applied first, then the one above it wraps that
#    result. At call time, the outermost wrapper runs first.
#
# 9. Such a wrapper may reject the call with TypeError because its parameters
#    do not match the original function's supported call patterns. *args and
#    **kwargs forward positional and keyword arguments.
#
# 10. One possible shape (left as a practice task): the factory validates and
#     stores limit, returns a decorate(function), which returns a wrapper using
#     *args/**kwargs and calls function(*args, **kwargs). See repeat() for the
#     three-level structure; add the message behavior yourself.


# ---------------------------------------------------------------------------
# 10. Mini practice — implement these yourself
# ---------------------------------------------------------------------------

# 1. Easy: Create @tag("DATA") that returns a function's result prefixed with
#    "[DATA] ". Test it on a function returning "ready".
#
# 2. Easy/Medium: Create @repeat_result(3) that calls a function three times
#    and returns the final result. Forward positional and keyword arguments.
#
# 3. Medium: Create @require_minimum(10) for a function that accepts one number.
#    Raise ValueError for a smaller input and otherwise return the function's
#    result. Preserve the wrapped function's metadata.
#
# 4. Tricky: Stack a decorator that uppercases a returned string with a
#    decorator factory that surrounds it with configurable characters. Try
#    both orders and explain the difference.
#
# 5. Interview-style: Implement @cache_result for a function that takes one
#    hashable argument. Decide what repeated calls should do, and explain one
#    limitation of your implementation. [LEARN LATER] Real caching requires
#    decisions about keys, memory, invalidation, and concurrency.


# ---------------------------------------------------------------------------
# 11. Roadmap connection and final checklist
# ---------------------------------------------------------------------------

# Decorators with arguments
#     -> functions, closures, wrappers, call/return behavior
#     -> framework routes, permissions, logging, and reusable policies
#     -> backend/API functions and shared AI/RAG pipeline behavior
#
# MUST KNOW: factory -> decorator -> wrapper; forward arguments; return results.
# GOOD TO KNOW: functools.wraps, closure configuration, decorator stacking.
# LEARN LATER: async decorators, typed decorators, production retries/caching.
# USED IN BACKEND: framework and cross-cutting function behavior.
# USED IN AI ENGINEERING: consistent wrappers around model/data operations.
# INTERVIEW IMPORTANT: decorator expansion, order, metadata, and return values.
