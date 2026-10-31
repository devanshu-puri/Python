# to turn a regular method into class method add decorator @classmethod

# class Employee:
#     num_of_emps = 0
#     raise_amount = 1.04

#     def __init__(self, first, last, pay): #email can be created from first and last
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first+'.'+last+'@company.com'
#         Employee.num_of_emps +=1

#     def fullname(self):
#         return '{} {}'.format(self.first, self.last) 

#     def apply_raise(self):
#         self.pay = int(self.pay * Employee.raise_amount) #or self.raise_amount)

#     #regular method automatically pass the instance , called self
#     #class method automatically pass the class as first argument, we use cls as class is a keyword
#     @classmethod
#     def set_raise_amt(cls, amount): #we are working in class instead of instance 
#         cls.raise_amount = amount #is same as Employee.set_raise_amt(1.05)

#     @classmethod
#     def from_string(cls, emp_str):#alternative constructor
#         first , last , day  = emp_str.split('-')
#         return cls(first, last, day)

# emp_1 = Employee('Corey', 'Schafer', 50000)
# emp_2 = Employee('Test' , 'User', 60000)

# Employee.set_raise_amt(1.05) #raise_amount turn from 1.04 to 1.05 

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Steve-Smith-30000'
# emp_str_3 = 'Jane-Doe-900000'

# #split them
# first, last, pay = emp_str_1.split('-')

# the above thing can be converted as classmethod and can be accessed as

# new_emp_1 = Employee.from_string(emp_str_1)

# '-------------------------------------------------------------------------------------------------------'

#static method dont pass anyting automatically, behave as regular function but logically work as class
# simple function take in a date and return whether that was work day

class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay): #email can be created from first and last
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'
        Employee.num_of_emps +=1

    def fullname(self):
        return '{} {}'.format(self.first, self.last) 

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount) #or self.raise_amount)

    #regular method automatically pass the instance , called self
    #class method automatically pass the class as first argument, we use cls as class is a keyword
    @classmethod
    def set_raise_amt(cls, amount): #we are working in class instead of instance 
        cls.raise_amount = amount #is same as Employee.set_raise_amt(1.05)

    @classmethod
    def from_string(cls, emp_str):#alternative constructor
        first , last , day  = emp_str.split('-')
        return cls(first, last, day)

    @staticmethod
    def is_workday(day): #directly pass the argument to work with
        #in python mon = 0, tues = 1 .....
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test' , 'User', 60000)

import datetime
my_date = datetime.date(2016, 7,10)

print(Employee.is_workday(my_date))


#========================= COrey python end ====================================================

"""Chapter 3: class methods and static methods.

Run this file with:
	python 10OOP.py/3CLassmethods_Staticmethods.py

Prerequisite: classes, self, instance variables, class variables, and methods.
"""


# ================================================================
# 1. THE THREE COMMON METHOD TYPES
# ================================================================
# Regular instance method: receives self and works with one object.
# Class method: receives cls and works with the class.
# Static method: receives neither self nor cls; it is a related utility.
class Employee:
	company = "Northwind"

	def __init__(self, name, salary):
		self.name = name
		self.salary = salary

	def describe(self):
		"""Instance method: uses data from one employee."""
		return f"{self.name} earns ${self.salary:,}."

	@classmethod
	def company_name(cls):
		"""Class method: reads class-level data."""
		return cls.company

	@staticmethod
	def is_valid_salary(salary):
		"""Static method: validates a value without object/class state."""
		return isinstance(salary, (int, float)) and salary >= 0


employee = Employee("Aisha", 85000)
print("Instance method:", employee.describe())
print("Class method:", Employee.company_name())
print("Static method:", Employee.is_valid_salary(85000))
print("Static method with bad input:", Employee.is_valid_salary(-10))


# ================================================================
# 2. HOW TO CALL EACH METHOD
# ================================================================
print("\nCalled through an instance:", employee.company_name())
print("Called through the class:", Employee.company_name())
print("Utility through the class:", Employee.is_valid_salary(100))

# A class method can be called through an instance, but calling it through the
# class communicates that the operation belongs to the class, not one object.


# ================================================================
# 3. WHY cls MATTERS: CLASSMETHODS SUPPORT SUBCLASSES
# ================================================================
class Notification:
	channel = "generic"

	@classmethod
	def channel_name(cls):
		return cls.channel


class EmailNotification(Notification):
	channel = "email"


print("\nParent channel:", Notification.channel_name())
print("Child channel:", EmailNotification.channel_name())


# Prefer cls inside a class method when the class may be subclassed.
class Document:
	format_name = "plain text"

	@classmethod
	def describe_format(cls):
		return f"{cls.__name__}: {cls.format_name}"


class MarkdownDocument(Document):
	format_name = "Markdown"


print("Subclass-aware method:", MarkdownDocument.describe_format())


# ================================================================
# 4. CLASSMETHOD AS AN ALTERNATE CONSTRUCTOR
# ================================================================
class User:
	def __init__(self, username, email):
		self.username = username
		self.email = email

	@classmethod
	def from_string(cls, text):
		"""Build a User from the compact form 'username,email'."""
		username, email = text.split(",", maxsplit=1)
		return cls(username.strip(), email.strip())

	def summary(self):
		return f"{self.username} <{self.email}>"


user = User.from_string("aisha, aisha@example.com")
print("\nAlternate constructor:", user.summary())


class AdminUser(User):
	def __init__(self, username, email):
		super().__init__(username, email)
		self.is_admin = True


admin = AdminUser.from_string("root, root@example.com")
print("Factory preserves subclass:", type(admin).__name__, admin.is_admin)


# ================================================================
# 5. MORE ALTERNATE CONSTRUCTORS: DICTIONARY AND DATABASE ROW SHAPES
# ================================================================
class Product:
	def __init__(self, name, price):
		self.name = name
		self.price = price

	@classmethod
	def from_dict(cls, data):
		return cls(name=data["name"], price=data["price"])

	@classmethod
	def from_database_row(cls, row):
		product_id, name, price = row
		product = cls(name, price)
		product.id = product_id
		return product


product1 = Product.from_dict({"name": "Keyboard", "price": 49.99})
product2 = Product.from_database_row((101, "Mouse", 24.99))
print("\nFrom dictionary:", product1.name, product1.price)
print("From database-shaped row:", product2.id, product2.name, product2.price)


# ================================================================
# 6. STATICMETHODS AS SMALL, RELATED UTILITIES
# ================================================================
class EmailAddress:
	def __init__(self, value):
		if not self.is_valid(value):
			raise ValueError("Invalid email address")
		self.value = value

	@staticmethod
	def is_valid(value):
		return isinstance(value, str) and "@" in value and "." in value.rsplit("@", 1)[-1]


print("\nValid email:", EmailAddress.is_valid("person@example.com"))
print("Invalid email:", EmailAddress.is_valid("not-an-email"))
address = EmailAddress("person@example.com")
print("Stored email:", address.value)


# A static method is still namespaced under EmailAddress, so the function is
# easy to find. It does not receive an automatic object or class argument.


# ================================================================
# 7. STATICMETHODS DO NOT RECEIVE self OR cls
# ================================================================
class TextTools:
	@staticmethod
	def normalize(text):
		return " ".join(text.strip().lower().split())


print("\nNormalized text:", TextTools.normalize("  Hello   PYTHON  "))

# This would fail because a static method has no automatic self argument:
# TextTools.normalize()  # TypeError: missing required argument: text


# ================================================================
# 8. CLASSMETHODS CAN CHANGE CLASS STATE
# ================================================================
class Job:
	active_jobs = 0

	def __init__(self, title):
		self.title = title
		type(self).active_jobs += 1

	@classmethod
	def reset_count(cls):
		cls.active_jobs = 0


Job("index documents")
Job("train model")
print("\nActive jobs:", Job.active_jobs)
Job.reset_count()
print("After reset:", Job.active_jobs)


# Be careful: changing class state globally affects all objects that use it.
# A request-specific value usually belongs on self, not on the class.


# ================================================================
# 9. CLASSMETHODS AND INHERITANCE: cls VS CLASS NAME
# ================================================================
class Parser:
	parser_name = "base parser"

	@classmethod
	def make(cls):
		return cls()

	def name(self):
		return self.parser_name


class JsonParser(Parser):
	parser_name = "JSON parser"


parser = JsonParser.make()
print("\nCreated subclass through cls:", parser.name())


class FixedParser:
	@classmethod
	def make(cls):
		return FixedParser()


class FixedJsonParser(FixedParser):
	pass


print("Hard-coded class result:", type(FixedJsonParser.make()).__name__)
print("Using cls is usually more extensible for factories.")


# ================================================================
# 10. DECORATOR ORDER AND A COMMON MISTAKE
# ================================================================
class Calculator:
	@staticmethod
	def add(first, second):
		return first + second

	@classmethod
	def label(cls):
		return cls.__name__


print("\nCalculator result:", Calculator.add(2, 3))
print("Calculator label:", Calculator.label())

# The decorators are part of the behavior. Without @classmethod, this method
# would be an ordinary function stored on the class and would not receive cls.


# ================================================================
# 11. WHEN TO CHOOSE WHICH METHOD
# ================================================================
"""
Use an instance method when:
- the operation needs self.name, self.price, or other object data.

Use a class method when:
- the operation needs cls or class-level configuration;
- you need an alternate constructor such as from_dict or from_string;
- subclass behavior should be preserved.

Use a static method when:
- the operation belongs conceptually to the class;
- it needs only its explicit arguments;
- putting it in the class gives the utility a clear home.

Use a module-level function when:
- the operation is not meaningfully related to one class;
- the function should be reused across unrelated classes.
"""


# ================================================================
# 12. COMMONLY SKIPPED DETAILS AND EDGE CASES
# ================================================================
"""
Important details:
- @classmethod automatically passes the calling class as cls.
- @staticmethod receives no automatic first argument.
- Class methods are inherited and normally create the subclass because they
  use cls(...), not a hard-coded class name.
- A class method can read or change class variables, but global class state
  should be changed intentionally.
- A static method can be called through the class or an instance, but it does
  not know which object was used.
- A class method is not the same thing as a regular function defined outside a
  class; the decorator changes binding behavior.

Common mistakes:
- Forgetting @classmethod and then writing def from_dict(cls, data).
- Writing self inside a static method even though no self is supplied.
- Using a static method when the operation actually needs instance state.
- Using a class method when a simple module function would be clearer.
- Returning FixedClass(...) inside a factory and breaking subclass creation.
- Passing unvalidated input to an alternate constructor.

Pythonic habits:
- Keep constructors simple and put alternate input shapes in class methods.
- Use static methods for focused validation or conversion helpers.
- Use cls instead of the class name in class factories.
- Raise a clear ValueError when constructor input is invalid.

[LEARN LATER] Descriptors and decorators explain the deeper mechanics behind
method binding. Recognize the behavior now; study the implementation later.

[LEARN LATER] Dependency injection frameworks often use classes and factories,
but first become comfortable choosing the correct method type.
"""


# ================================================================
# 13. USED LATER GLIMPSE
# ================================================================
"""
Concept: class methods as alternate constructors
Why it matters later: external data comes in different shapes.
Where: FastAPI request models, database rows, JSON/API payloads, config files.

Concept: cls and subclass-aware factories
Why it matters later: one base interface can create specialized implementations.
Where: parsers, database repositories, model loaders, plugin systems.

Concept: static validation and conversion helpers
Why it matters later: reusable input checks keep related logic organized.
Where: API validation, file parsing, preprocessing, model input preparation.

Concept: class-level configuration
Why it matters later: shared defaults can make service behavior consistent.
Where: API clients, retry defaults, model names, serialization settings.

Backend: a `from_dict` class method can build an object from request data.
FastAPI: factories and validators may prepare request or response objects.
Databases: `from_database_row` resembles converting query results to objects.
Data processing: static helpers normalize text or validate records.
AI/ML: class methods can load a model from a path or configuration mapping.
RAG/LLM: loaders may create document objects from files or metadata records.
Async/concurrent: [LEARN LATER] factories may create async service clients,
but async behavior is a later topic.
Distributed systems: [LEARN LATER] class state is process-local, so it is not
automatically shared between workers or machines.
"""


# ================================================================
# 14. IMPORTANT TECHNIQUES TO RECOGNIZE
# ================================================================
"""
Technique                 This chapter's connection
@classmethod              receives cls and supports class-aware factories
@staticmethod             related utility with no automatic argument
cls(...)                  create the active class, including subclasses
super().__init__(...)     initialize inherited instance state
isinstance(...)           validate values or object types
type(obj).__name__        inspect the concrete class while debugging
str.split(..., maxsplit)  parse compact constructor input
raise ValueError(...)     reject invalid constructor input clearly
*args / **kwargs          [LEARN LATER] flexible factory inputs
decorators                [LEARN LATER] reusable behavior around functions
"""


# ================================================================
# 15. MINI PRACTICE: DO THESE WITHOUT LOOKING AT A SOLUTION
# ================================================================
"""
1. Easy: Create a `Temperature` class with a static method that converts
   Celsius to Fahrenheit. Test 0 C -> 32 F.

2. Easy/Medium: Create a `Book` class with `from_string("title|author")` as a
   class method. Return a Book object and print its fields.

3. Medium: Create a `User` class with `from_dict` and `is_valid_username`.
   Make the factory call the static validation method.

4. Tricky: Create a base `Report` class and a `CsvReport` subclass. Implement
   a class method `empty()` that returns the active subclass, not always Report.

5. Interview-style: Decide whether each operation should be an instance method,
   class method, static method, or module function:
   - calculate one order's total;
   - create an order from a JSON-like dictionary;
   - check whether a product code has the correct format;
   - load a class-specific default configuration.
"""


# ================================================================
# 16. INTERVIEW / MIND-TWISTING QUESTIONS
# ================================================================
"""
Question 1 - Easy
What automatic argument does an instance method receive?

Question 2 - Easy
What automatic argument does a class method receive? What does a static method
receive automatically?

Question 3 - Easy output prediction
class Counter:
	value = 0

	@classmethod
	def increment(cls):
		cls.value += 1

Counter.increment()
print(Counter.value)

Question 4 - Medium debugging
Why does this fail, and how should it be fixed?
class User:
	@classmethod
	def from_text(cls, text):
		return User(text)

Question 5 - Medium output prediction
class Base:
	name = "base"

	@classmethod
	def get_name(cls):
		return cls.name

class Child(Base):
	name = "child"

print(Child.get_name())

Question 6 - Medium
When is a module-level function clearer than a static method?

Question 7 - Tricky
Why is `cls()` usually preferable to `BaseClass()` inside an alternate
constructor?

Question 8 - Tricky output prediction
class Tools:
	@staticmethod
	def identity(value):
		return value

tool = Tools()
print(Tools.identity(3), tool.identity(4))

Question 9 - Interview-style
Design `Model.from_config(config)` and explain why it should be a class method
instead of a static method.
"""


# ================================================================
# 17. ANSWERS + EXPLANATIONS
# ================================================================
"""
1. An instance method receives self, the object used for the call.

2. A class method receives cls, the class used for the call. A static method
   receives no automatic argument.

3. It prints 1. The method changes the class variable through cls.

4. It may work for User itself, but it hard-codes User and prevents subclasses
   from being created correctly. Use `return cls(text)`.

5. It prints child. cls is Child when Child.get_name() is called.

6. Use a module-level function when the logic is not conceptually owned by a
   class. A static method is useful when the class provides a clear namespace.

7. cls() creates the class that made the call, so inherited factories preserve
   subclass behavior.

8. It prints `3 4`. A static method does not receive self, even when called
   through an instance.

9. It should be a class method because it needs cls to construct and return the
   active model class, including any specialized subclass.
"""


# ================================================================
# 18. COMMON INTERVIEW TRAPS
# ================================================================
"""
- @classmethod is required when the first parameter is cls.
- @staticmethod is required when no automatic self or cls should be passed.
- `self` and `cls` are conventional names, but the decorator controls binding.
- A static method cannot access self or cls unless they are passed explicitly.
- A class method called on a subclass receives the subclass as cls.
- Hard-coding the base class inside a factory can break inheritance.
- Class methods can mutate shared class state; do not confuse it with request data.
- A static method may be callable through an instance, but that does not make it
  an instance method.
- `classmethod` and `staticmethod` are decorators, not ordinary method names.
"""


# ================================================================
# 19. FUTURE ROADMAP CONNECTION
# ================================================================
"""
CURRENT CHAPTER: class methods and static methods
		↓
WHAT I LEARNED: cls-aware factories and related utility functions
		↓
WHERE IT APPEARS LATER: API models, database conversion, loaders, validators
		↓
BACKEND / AI APPLICATION: create reliable objects from requests, rows, files,
and model configuration while keeping shared and object-specific data separate.
"""


if __name__ == "__main__":
	assert employee.describe() == "Aisha earns $85,000."
	assert Employee.company_name() == "Northwind"
	assert Employee.is_valid_salary(0) is True
	assert Employee.is_valid_salary(-1) is False
	assert EmailNotification.channel_name() == "email"
	assert isinstance(user, User)
	assert isinstance(admin, AdminUser)
	assert product2.id == 101
	assert parser.name() == "JSON parser"
	assert type(JsonParser.make()).__name__ == "JsonParser"
	assert Calculator.add(2, 3) == 5
	print("\nChapter checks passed.")
