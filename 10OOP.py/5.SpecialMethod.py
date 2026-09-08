"""Chapter 5: special methods, also called dunder methods.

Run this file with:
	python 10OOP.py/5.SpecialMethod.py

Prerequisite: classes, methods, class variables, class methods, and inheritance.
"""


# ================================================================
# 1. WHAT ARE SPECIAL METHODS?
# ================================================================
# Special methods have names that start and end with two underscores.
# Python calls them behind familiar syntax such as str(obj), len(obj), obj + x,
# obj == other, for item in obj, and with obj.
class User:
	def __init__(self, username):
		self.username = username

	def __str__(self):
		return f"User: {self.username}"


user = User("aisha")
print("Special method through str():", str(user))
print("Normal attribute:", user.username)


# Prefer calling the normal Python operation (str, len, +, ==) rather than
# calling a dunder method directly in application code.


# ================================================================
# 2. __str__: A FRIENDLY DISPLAY FOR USERS
# ================================================================
class Product:
	def __init__(self, name, price):
		self.name = name
		self.price = price

	def __str__(self):
		return f"{self.name} (${self.price:.2f})"


product = Product("Keyboard", 49.99)
print("\nstr(product):", str(product))
print("print(product):", product)


# __str__ should be readable. It is useful for logs, command-line output, and
# messages shown while debugging.


# ================================================================
# 3. __repr__: AN UNAMBIGUOUS DEBUGGING REPRESENTATION
# ================================================================
class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __repr__(self):
		return f"Point(x={self.x!r}, y={self.y!r})"


point = Point(3, 4)
print("\nrepr(point):", repr(point))
print("List uses repr for its items:", [point])


# repr() is aimed at developers and should reveal useful state. The !r in an
# f-string asks Python to use repr for a value.


# ================================================================
# 4. __str__ AND __repr__ TOGETHER
# ================================================================
class Order:
	def __init__(self, order_id, status):
		self.order_id = order_id
		self.status = status

	def __str__(self):
		return f"Order {self.order_id}: {self.status}"

	def __repr__(self):
		return f"Order(order_id={self.order_id!r}, status={self.status!r})"


order = Order(101, "processing")
print("\nFriendly order:", str(order))
print("Debug order:", repr(order))


# If __str__ is missing, str(obj) falls back to __repr__ when __repr__ exists.
# If neither is defined, Python shows a default class-and-memory representation.


# ================================================================
# 5. __len__: MAKE len(obj) MEANINGFUL
# ================================================================
class Playlist:
	def __init__(self, songs):
		self.songs = list(songs)

	def __len__(self):
		return len(self.songs)


playlist = Playlist(["Intro", "Focus", "Deep Work"])
print("\nPlaylist length:", len(playlist))


# __len__ must return a non-negative integer. Returning a string or a negative
# number raises an error when len() is called.


# ================================================================
# 6. __add__: DEFINE + FOR A DOMAIN OBJECT
# ================================================================
class Money:
	def __init__(self, amount, currency="USD"):
		self.amount = amount
		self.currency = currency

	def __add__(self, other):
		if not isinstance(other, Money):
			return NotImplemented
		if self.currency != other.currency:
			raise ValueError("Cannot add different currencies")
		return Money(self.amount + other.amount, self.currency)

	def __repr__(self):
		return f"Money({self.amount!r}, {self.currency!r})"


total = Money(10) + Money(7.5)
print("\nMoney addition:", total)


# Returning NotImplemented lets Python try the other operand's reflected method
# or produce a suitable TypeError. It is better than returning False or None.


# ================================================================
# 7. COMPARISON: __eq__ AND __lt__
# ================================================================
class Task:
	def __init__(self, task_id, priority):
		self.task_id = task_id
		self.priority = priority

	def __eq__(self, other):
		if not isinstance(other, Task):
			return NotImplemented
		return self.task_id == other.task_id

	def __lt__(self, other):
		if not isinstance(other, Task):
			return NotImplemented
		return self.priority < other.priority

	def __repr__(self):
		return f"Task({self.task_id!r}, priority={self.priority!r})"


task1 = Task("train-model", 2)
task2 = Task("train-model", 1)
task3 = Task("serve-api", 3)
print("\nEqual task IDs:", task1 == task2)
print("Different task IDs:", task1 == task3)
print("Priority comparison:", task2 < task3)
print("Sorted tasks:", sorted([task1, task3, task2]))


# Equality should represent the identity or value rule that makes sense for
# the domain. Here task_id identifies a task, so priority does not affect ==.


# ================================================================
# 8. __bool__: CONTROL TRUTHINESS
# ================================================================
class Response:
	def __init__(self, status_code, data=None):
		self.status_code = status_code
		self.data = data

	def __bool__(self):
		return 200 <= self.status_code < 300


success = Response(200, {"ok": True})
failure = Response(500, {"ok": False})
print("\nSuccessful response is truthy:", bool(success))
print("Failed response is truthy:", bool(failure))
if success:
	print("if response: success branch")


# Keep truthiness intuitive. If an object can be both empty and invalid, an
# explicit property such as response.is_success is often clearer.


# ================================================================
# 9. __getitem__, __setitem__, AND __contains__
# ================================================================
class Config:
	def __init__(self, values):
		self._values = dict(values)

	def __getitem__(self, key):
		return self._values[key]

	def __setitem__(self, key, value):
		self._values[key] = value

	def __contains__(self, key):
		return key in self._values

	def __repr__(self):
		return f"Config({self._values!r})"


config = Config({"timeout": 5, "region": "eu-west-1"})
print("\nConfig indexing:", config["timeout"])
config["timeout"] = 10
print("Config assignment:", config)
print("Config membership:", "region" in config)


# These methods make an object feel mapping-like. Use them only when the
# behavior is genuinely natural; otherwise normal named methods are clearer.


# ================================================================
# 10. __iter__: MAKE AN OBJECT ITERABLE
# ================================================================
class Batch:
	def __init__(self, records):
		self.records = list(records)

	def __iter__(self):
		return iter(self.records)

	def __len__(self):
		return len(self.records)


batch = Batch([{"id": 1}, {"id": 2}])
print("\nIterating over Batch:")
for record in batch:
	print(record)
print("Batch length:", len(batch))


# Returning iter(self.records) delegates iteration to the contained list.
# This is simpler than manually implementing __next__ for ordinary containers.


# ================================================================
# 11. __call__: MAKE AN OBJECT CALLABLE
# ================================================================
class Multiplier:
	def __init__(self, factor):
		self.factor = factor

	def __call__(self, value):
		return value * self.factor


double = Multiplier(2)
print("\nCallable object:", double(6))
print("Is callable:", callable(double))


# Callable objects can store configuration while still being used like a
# function. [LEARN LATER] This appears in callbacks and decorators.


# ================================================================
# 12. __enter__ AND __exit__: BASIC CONTEXT MANAGER
# ================================================================
class ActivityLog:
	def __enter__(self):
		print("\nLog started")
		return self

	def write(self, message):
		print("LOG:", message)

	def __exit__(self, exc_type, exc_value, traceback):
		print("Log closed")
		return False


with ActivityLog() as log:
	log.write("request received")


# `with` guarantees cleanup when the block finishes, including many error
# cases. [LEARN LATER] Files, locks, and database transactions use this pattern.


# ================================================================
# 13. __new__ AND __del__: RECOGNIZE, DO NOT FOCUS YET
# ================================================================
"""
__new__ creates an object before __init__ initializes it. Most application code
does not need to override it.

__del__ may run when an object is collected, but its timing is not a reliable
cleanup strategy. Prefer a context manager or an explicit close method.

[LEARN LATER] These methods matter for advanced object creation and resource
management. Recognize the names now; do not build designs around them yet.
"""


# ================================================================
# 14. SPECIAL METHODS AND INHERITANCE
# ================================================================
class BaseDocument:
	def __repr__(self):
		return f"{type(self).__name__}()"


class TextDocument(BaseDocument):
	pass


print("\nInherited special method:", repr(TextDocument()))


class NamedDocument(BaseDocument):
	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return f"NamedDocument(name={self.name!r})"


print("Overridden special method:", repr(NamedDocument("notes")))


# Dunder methods follow the same inheritance and overriding rules as normal
# methods.


# ================================================================
# 15. COMMONLY SKIPPED DETAILS AND EDGE CASES
# ================================================================
"""
MUST KNOW:
- Dunder methods connect user-defined objects to normal Python syntax.
- __str__ is friendly; __repr__ is mainly for developers and debugging.
- __len__ powers len(obj), and must return a non-negative integer.
- __add__ powers + and should return a new compatible value when possible.
- __eq__ controls value equality; it does not change `is` identity checks.
- __iter__ powers for-loops and many tools that consume iterables.
- __getitem__ powers indexing and subscription syntax such as obj[key].
- __call__ makes an instance usable like a function.
- __enter__ and __exit__ support the with statement.

Common mistakes:
- Returning a non-string from __str__ or __repr__.
- Returning None from __len__ or returning a negative length.
- Returning False from __add__ when the other type is unsupported instead of
  returning NotImplemented.
- Defining __eq__ without thinking about how objects should be identified.
- Making __bool__ surprising, so valid objects behave as false unexpectedly.
- Implementing __iter__ with `return self` without also implementing __next__.
- Using __del__ for important cleanup.
- Calling dunder methods directly instead of using normal Python operations.
- Adding many special methods merely to make a class look clever.

Pythonic habits:
- Implement only methods that match the natural meaning of your object.
- Keep __repr__ short, useful, and stable enough for debugging.
- Prefer normal named methods for complex operations.
- Return NotImplemented for unsupported binary operand types.
- Use context managers for cleanup and resource lifetimes.

Important identity rule:
`a == b` asks whether values are equal; `a is b` asks whether they are the
same object. Special methods usually affect ==, not is.
"""


# ================================================================
# 16. USED LATER GLIMPSE
# ================================================================
"""
Concept: __repr__ and __str__
Why it matters later: useful logs and readable debugging output reduce diagnosis time.
Where: API objects, database records, model configuration, background jobs.

Concept: __eq__ and ordering methods
Why it matters later: compare domain records, sort jobs, and test returned data.
Where: database entities, queues, evaluation results, data processing.

Concept: __iter__ and __getitem__
Why it matters later: custom containers can behave like API results or datasets.
Where: pagination, batches, document collections, token/chunk processing.

Concept: __call__
Why it matters later: configured objects can be passed wherever a function is expected.
Where: callbacks, preprocessing steps, scoring functions, AI pipelines.

Concept: context-manager methods
Why it matters later: resources need reliable setup and cleanup.
Where: files, database sessions, locks, HTTP clients, transactions.

Backend/FastAPI: readable representations help logs, while context managers
help manage request-scoped resources.
Databases: equality and representation help entity tests and query debugging.
Data processing: iterable batches and indexable records fit pipeline code.
AI/ML: callable preprocessors and model wrappers can use the same interface as functions.
RAG/LLM: iterable document batches and readable chunk objects help retrieval pipelines.
Async/concurrent: [LEARN LATER] async context managers manage async clients and locks.
Distributed systems: [LEARN LATER] local dunder behavior does not make objects
serializable or transferable across processes; serialization needs explicit design.
"""


# ================================================================
# 17. IMPORTANT TECHNIQUES TO RECOGNIZE
# ================================================================
"""
Technique                    This chapter's connection
__str__ / __repr__           friendly versus debugging representation
__len__                      integrate with len()
__add__                      integrate with +
__eq__ / __lt__              equality and sorting
__bool__                     integrate with if and bool()
__getitem__ / __setitem__    index and assign with []
__contains__                 integrate with `in`
__iter__                     integrate with for-loops
__call__                     make configured objects callable
__enter__ / __exit__         integrate with with
NotImplemented               signal unsupported operand types
datamodel protocols          [LEARN LATER] Python's deeper object model
"""


# ================================================================
# 18. MINI PRACTICE: DO THESE WITHOUT LOOKING AT A SOLUTION
# ================================================================
"""
1. Easy: Create a `Book` class with __str__ returning its title and author.

2. Easy/Medium: Create a `Cart` class with __len__ and __contains__ so that
   len(cart) and "book" in cart work naturally.

3. Medium: Create a `Vector` class with __add__ and __repr__. Adding two
   vectors should return a new Vector.

4. Tricky: Create a `JobQueue` class with __iter__ and __bool__. An empty queue
   should be false, and a non-empty queue should be iterable.

5. Interview-style: Create a context manager that prints "connected" on entry
   and "disconnected" on exit. Demonstrate that it works with a with block.
"""


# ================================================================
# 19. INTERVIEW / MIND-TWISTING QUESTIONS
# ================================================================
"""
Question 1 - Easy
What is a special method, and why does Python call it a dunder method?

Question 2 - Easy output prediction
class Item:
	def __str__(self):
		return "item"

print(Item())

Question 3 - Easy/Medium
What is the difference between __str__ and __repr__?

Question 4 - Medium output prediction
class Box:
	def __len__(self):
		return 3

print(len(Box()))

Question 5 - Medium debugging
Why is this invalid?
class Bad:
	def __str__(self):
		return 123

Question 6 - Medium
Why should __add__ return NotImplemented for an unsupported type?

Question 7 - Tricky output prediction
class Value:
	def __eq__(self, other):
		return True

a = Value()
b = Value()
print(a == b, a is b)

Question 8 - Tricky
What must an object implement if __iter__ returns self?

Question 9 - Interview-style
When would __enter__ and __exit__ be better than an explicit open/close pair?
"""


# ================================================================
# 20. ANSWERS + EXPLANATIONS
# ================================================================
"""
1. A special method is a hook that lets a user-defined object participate in
   built-in Python operations. Dunder refers to double underscores.

2. It prints `item` because print() uses str(), which calls __str__.

3. __str__ is for a friendly display. __repr__ is for a useful developer-facing
   representation and is used inside containers such as lists.

4. It prints 3 because len(Box()) calls Box.__len__().

5. __str__ must return a string. Returning 123 causes TypeError when str() or
   print() tries to use it.

6. NotImplemented tells Python that this operand type is unsupported, allowing
   reflected operations or a proper TypeError instead of a misleading result.

7. It prints `True False`. __eq__ controls value equality; `a` and `b` are still
   two different objects, so identity is false.

8. It must implement __next__ and raise StopIteration when iteration finishes.
   Usually returning iter(self.items) is simpler for container classes.

9. A context manager makes cleanup automatic when the block exits, including
   many exception paths, so resources are less likely to remain open.
"""


# ================================================================
# 21. COMMON INTERVIEW TRAPS
# ================================================================
"""
- __str__ and __repr__ must return strings, not any other value.
- __repr__ is commonly visible inside lists and dictionaries.
- __eq__ changes ==, but it does not make two objects identical for is.
- __len__ must return a non-negative integer.
- __bool__ can make an object false in an if statement even when it exists.
- Unsupported arithmetic should return NotImplemented, not False.
- __iter__ and __next__ are separate parts of the iterator protocol.
- A with block calls __enter__ before the body and __exit__ afterward.
- __del__ is not a reliable replacement for a context manager.
- Special methods should match the natural behavior of the object.
"""


# ================================================================
# 22. FUTURE ROADMAP CONNECTION
# ================================================================
"""
CURRENT CHAPTER: Special methods
		↓
WHAT I LEARNED: connect custom objects to Python syntax and protocols
		↓
WHERE IT APPEARS LATER: models, containers, logs, resources, data pipelines
		↓
BACKEND / AI APPLICATION: domain objects can behave naturally in API, database,
and AI pipeline code while keeping setup, comparison, and cleanup predictable.
"""


if __name__ == "__main__":
	assert str(product) == "Keyboard ($49.99)"
	assert repr(point) == "Point(x=3, y=4)"
	assert len(playlist) == 3
	assert total.amount == 17.5
	assert task1 == task2
	assert task2 < task3
	assert bool(success) is True
	assert bool(failure) is False
	assert config["timeout"] == 10
	assert "region" in config
	assert list(batch) == [{"id": 1}, {"id": 2}]
	assert double(6) == 12
	assert repr(TextDocument()) == "TextDocument()"
	print("\nChapter checks passed.")