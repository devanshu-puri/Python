"""Type hints for a small user directory.

Run: python intermediate/Typehint.py

Type hints describe the values code expects and returns. They help you, other
programmers, and editor/type-checker tools understand code. Python itself does
not enforce these hints when the program runs.
"""

# SCENARIO
# A small backend service receives a user's details, stores user records, and
# looks them up. We will describe the shapes of the values as they move through
# the program.


# 1. SIMPLE TYPES
# These names tell readers what kind of value each variable should hold.
user_name: str = "Mina"       # text
user_id: int = 101             # whole number
is_active: bool = True         # True or False


# 2. FUNCTION INPUTS AND RETURN VALUE
# Read this as: takes a string, returns a string.
def make_greeting(name: str) -> str:
    return f"Welcome, {name}!"


print(make_greeting(user_name))


# 3. COLLECTIONS
# list[str] means a list whose items are strings.
# dict[int, str] means keys are integers and values are strings.
skills: list[str] = ["Python", "SQL"]
user_names_by_id: dict[int, str] = {101: "Mina", 102: "Arun"}


# A tuple can describe a fixed group of values: (user ID, user name).
user_summary: tuple[int, str] = (user_id, user_name)


# 4. DESCRIBE A RECORD WITH A CLASS
# Each User object has fields with known types. This is a common way to model
# structured data before learning dedicated validation libraries.
class User:
    def __init__(self, user_id: int, name: str, active: bool) -> None:
        self.user_id = user_id
        self.name = name
        self.active = active


def display_user(user: User) -> str:
    status: str = "active" if user.active else "inactive"
    return f"{user.user_id}: {user.name} ({status})"


user = User(user_id=101, name="Mina", active=True)
print(display_user(user))


# 5. OPTIONAL / MISSING RESULTS
# A lookup might not find a user. int | None means the result is either an
# integer ID or None. Check for None before using it as an int.
def find_user_id(name: str, directory: dict[str, int]) -> int | None:
    return directory.get(name)


ids_by_name: dict[str, int] = {"Mina": 101, "Arun": 102}
found_id = find_user_id("Mina", ids_by_name)

if found_id is not None:
    print(f"Found user ID: {found_id}")
else:
    print("User not found")


# 6. INPUT TYPE AND RETURN TYPE CAN DIFFER
# Convert untrusted text (such as a URL path parameter) after checking it.
# Hints document that this function accepts text and returns an int or None;
# the explicit validation is what makes conversion safe.
def parse_user_id(raw_value: str) -> int | None:
    if not raw_value.isdecimal():
        return None
    return int(raw_value)


print(parse_user_id("101"))  # 101
print(parse_user_id("abc"))  # None


# 7. NONE RETURN TYPE
# -> None says this function is used for its side effect (printing), not for a
# value that the caller should use.
def print_user(user: User) -> None:
    print(display_user(user))


print_user(user)


# 8. TESTING THE BEHAVIOR
# Hints alone do not prove the function is correct. Test expected values and
# edge cases just as you would test unannotated Python code.
assert make_greeting("Mina") == "Welcome, Mina!"
assert find_user_id("Mina", ids_by_name) == 101
assert find_user_id("Unknown", ids_by_name) is None
assert parse_user_id("25") == 25
assert parse_user_id("twenty-five") is None


# LEARNING CHECKLIST
# [ ] Read parameter hints and -> return hints.
# [ ] Write hints for str, int, float, bool, and None.
# [ ] Hint lists, dictionaries, and fixed tuples.
# [ ] Use ClassName as the hint when a function expects one of your objects.
# [ ] Use T | None when a value may be missing; check for None before use.
# [ ] Test normal inputs, missing results, and invalid external input.
# [ ] Run a static type checker (for example, mypy or pyright) to find hint
#     mismatches; Python running successfully does not perform that check.
#
# IMPORTANT LIMITS
# - Type hints are not runtime validation. User input still needs checking.
# - A hint can be wrong; a static type checker can report many such mistakes.
# - Do not annotate every temporary variable if the value is already obvious.
# - For now, focus on the types used above. Generics, Protocol, overloads,
#   TypeVar, and elaborate typing imports can wait until a project needs them.
