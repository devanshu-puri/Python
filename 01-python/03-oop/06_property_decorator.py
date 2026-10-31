class Employee:
    def __init__(self, first, last): #email can be created from first and last
        self.first = first
        self.last = last

    @property # we are defiing email( .email() ) as method but accessing as attribute .email
    def email(self):
            return '{} {}@email.com'.format(self.first, self.last)  

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Deleted the name ')
        self.first = None
        self.last = None

emp_1 = Employee('Corey', 'Schafer')
emp_1.fullname = 'Corey Schafer'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname) #take this full name to below of fullname_setter and then split it into first and last 
del emp_1.fullname

#================================= corey python end ===================================

"""Chapter 6: the @property decorator.

Run this file with:
	python 10OOP.py/6PropertyDecorator.py

Prerequisite: classes, inheritance, special methods, and basic decorators.
"""


# ================================================================
# 1. THE PROBLEM: METHOD CALLS VS ATTRIBUTE SYNTAX
# ================================================================
class Employee:
	def __init__(self, first, last):
		self.first = first
		self.last = last

	def fullname(self):
		return f"{self.first} {self.last}"


employee = Employee("Aisha", "Khan")
print("Method call:", employee.fullname())


# A property lets callers use attribute syntax for a value that is computed by
# a method: employee.fullname instead of employee.fullname().


# ================================================================
# 2. BASIC @property: A COMPUTED, READ-ONLY ATTRIBUTE
# ================================================================
class Person:
	def __init__(self, first, last):
		self.first = first
		self.last = last

	@property
	def fullname(self):
		return f"{self.first} {self.last}"


person = Person("Daniel", "Lee")
print("\nComputed property:", person.fullname)
person.first = "Dan"
print("Property updates from source data:", person.fullname)


# `fullname` looks like an attribute to the caller but runs code on access.
# This property has no setter, so it is read-only through normal assignment.


# ================================================================
# 3. @property WITH A SETTER: VALIDATE ASSIGNMENT
# ================================================================
class User:
	def __init__(self, email):
		self.email = email

	@property
	def email(self):
		return self._email

	@email.setter
	def email(self, value):
		if not isinstance(value, str) or "@" not in value:
			raise ValueError("email must contain @")
		self._email = value.strip().lower()


user = User("Aisha@EXAMPLE.COM")
print("\nValidated email:", user.email)
user.email = "new@example.com"
print("Updated email:", user.email)


# `_email` is the backing attribute. The public name `email` is controlled by
# the property, so every assignment passes through the setter.


# ================================================================
# 4. THE RECURSION MISTAKE
# ================================================================
class SafeName:
	def __init__(self, name):
		self.name = name

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, value):
		if not value:
			raise ValueError("name cannot be empty")
		self._name = value.strip()


safe_name = SafeName(" Aisha ")
print("\nBacking attribute value:", safe_name._name)
print("Public property value:", safe_name.name)


# Do not write self.name = value inside the name setter: that calls the setter
# again forever. Store the value in a different backing attribute such as _name.


# ================================================================
# 5. READ-ONLY PROPERTY WITH NO SETTER
# ================================================================
class Order:
	def __init__(self, quantity, unit_price):
		self.quantity = quantity
		self.unit_price = unit_price

	@property
	def total(self):
		return self.quantity * self.unit_price


order = Order(3, 19.99)
print("\nRead-only total:", order.total)

try:
	order.total = 100
except AttributeError as error:
	print("Read-only assignment error:", type(error).__name__)


# A property without a setter is a good fit for a value derived from other
# fields. Callers should change quantity or unit_price instead.


# ================================================================
# 6. SETTER VALIDATION AND NORMALIZATION
# ================================================================
class Product:
	def __init__(self, name, price):
		self.name = name
		self.price = price

	@property
	def price(self):
		return self._price

	@price.setter
	def price(self, value):
		if not isinstance(value, (int, float)):
			raise TypeError("price must be a number")
		if value < 0:
			raise ValueError("price cannot be negative")
		self._price = round(value, 2)


product = Product("Keyboard", 49.999)
print("\nNormalized price:", product.price)
product.price = 55.5
print("Updated price:", product.price)


# Setters are useful when the rules must apply both during construction and
# during later updates.


# ================================================================
# 7. @property WITH A DELETER
# ================================================================
class TemporaryToken:
	def __init__(self, token):
		self.token = token

	@property
	def token(self):
		return self._token

	@token.setter
	def token(self, value):
		if not value:
			raise ValueError("token cannot be empty")
		self._token = value

	@token.deleter
	def token(self):
		print("Token deleted")
		del self._token


temporary_token = TemporaryToken("abc123")
print("\nToken before delete:", temporary_token.token)
del temporary_token.token
print("Token exists after delete:", hasattr(temporary_token, "_token"))


# Deleters are less common than getters and setters. Use one when deletion is a
# meaningful, controlled operation rather than simply exposing __dict__.


# ================================================================
# 8. @property IS A DESCRIPTOR CREATED BY A DECORATOR
# ================================================================
class Temperature:
	def __init__(self, celsius):
		self.celsius = celsius

	@property
	def fahrenheit(self):
		return self.celsius * 9 / 5 + 32


temperature = Temperature(0)
print("\nCelsius:", temperature.celsius)
print("Computed Fahrenheit:", temperature.fahrenheit)

# The decorator replaces the method with a property object on the class.
print("Property object:", type(Temperature.__dict__["fahrenheit"]).__name__)


# [LEARN LATER] Descriptors explain the full implementation of property. For
# now, remember that @property changes method access into attribute access.


# ================================================================
# 9. PROPERTY IN INHERITANCE
# ================================================================
class Account:
	def __init__(self, balance):
		self.balance = balance

	@property
	def status(self):
		return "healthy" if self.balance >= 0 else "overdrawn"


class PremiumAccount(Account):
	@property
	def status(self):
		return "premium " + super().status


account = PremiumAccount(100)
print("\nInherited and overridden property:", account.status)


# Properties follow normal inheritance rules. A child can override a property
# and use super() when it wants to extend the parent's result.


# ================================================================
# 10. PROPERTY VS SIMPLE ATTRIBUTE VS METHOD
# ================================================================
"""
Simple attribute:
	user.name
	Use when storing plain data needs no validation or computation.

Property:
	user.email
	Use when attribute syntax is natural but access or assignment needs logic.

Method:
	user.send_email()
	Use when an action is performed, especially when arguments or side effects
	make the operation feel like an action.

Good property candidates: full_name, total, status, normalized values.
Poor property candidates: network calls, database queries, expensive model
inference, or actions that surprise the reader when accessed.
"""


# ================================================================
# 11. PROPERTY AND BACKWARD-COMPATIBLE REFACTORING
# ================================================================
class LegacyUser:
	def __init__(self, first, last):
		self.first = first
		self.last = last

	@property
	def fullname(self):
		return f"{self.first} {self.last}"


legacy_user = LegacyUser("Sam", "Taylor")
print("\nAttribute-style API:", legacy_user.fullname)


# A property can add validation or computation later without changing the
# calling syntax used by the rest of the program.


# ================================================================
# 12. CLASS PROPERTY AND STATICMETHOD REMINDER
# ================================================================
class ApiConfig:
	default_timeout = 5

	def __init__(self, timeout=None):
		self.timeout = timeout

	@property
	def effective_timeout(self):
		return self.timeout if self.timeout is not None else type(self).default_timeout

	@staticmethod
	def valid_timeout(value):
		return isinstance(value, (int, float)) and value > 0


config = ApiConfig()
custom_config = ApiConfig(20)
print("\nDefault effective timeout:", config.effective_timeout)
print("Custom effective timeout:", custom_config.effective_timeout)
print("Static validation:", ApiConfig.valid_timeout(10))


# This combines previous chapters: a property reads instance/class state, while
# a static method validates an explicit value without needing self or cls.


# ================================================================
# 13. COMMONLY SKIPPED DETAILS AND EDGE CASES
# ================================================================
"""
MUST KNOW:
- @property lets a method be accessed like an attribute.
- A getter is written with @property.
- A setter uses @name.setter and usually writes to _name.
- A deleter uses @name.deleter and controls `del obj.name`.
- A property can be read-only when no setter exists.
- The getter, setter, and deleter must use the same property name.
- Validation in a setter applies during __init__ if __init__ assigns self.name.
- Properties are inherited and can be overridden.

Common mistakes:
- Calling a property like a method: user.email().
- Assigning to a read-only property.
- Recursion from self.email = value inside the email setter.
- Bypassing validation with direct access to _email.
- Putting slow I/O or surprising side effects in a getter.
- Forgetting that a getter can raise exceptions when the attribute is read.
- Using a property just to hide a simple public value with no behavior.

Pythonic habits:
- Use properties to preserve a natural attribute-style API.
- Keep getters fast and predictable.
- Validate and normalize at the boundary in setters or constructors.
- Use a leading underscore to signal an implementation detail, not strict privacy.
- Prefer explicit methods for actions such as refresh(), save(), or send().

Important edge case:
If a property has no setter, assigning to it raises AttributeError even if the
class also has a similarly named value elsewhere. A property controls that name.

[LEARN LATER] `property(getter, setter, deleter)` is the functional form, but the
decorator form is easier to read and is the usual style.
"""


# ================================================================
# 14. USED LATER GLIMPSE
# ================================================================
"""
Concept: validation in setters
Why it matters later: invalid state can be rejected at the object boundary.
Where: API request objects, database entities, configuration classes.

Concept: computed properties
Why it matters later: callers can read derived values without duplicating logic.
Where: order totals, account status, model metadata, pagination information.

Concept: read-only properties
Why it matters later: expose safe derived or identity values without allowing
accidental reassignment.
Where: record IDs, response status, model names, document metadata.

Concept: property and inheritance
Why it matters later: specialized services can adjust shared state rules.
Where: account types, storage adapters, API client configuration.

Backend/FastAPI: properties can normalize and expose request or response data,
but route handlers should not hide network calls inside getters.
Databases: entity properties can validate fields before persistence.
Data processing: computed properties can expose cleaned or derived columns.
AI/ML: model wrappers may expose device, input shape, or metadata properties.
RAG/LLM: document objects can expose normalized text or chunk metadata.
Async/concurrent: [LEARN LATER] properties should not secretly perform async
work because property access cannot be awaited in the normal syntax.
Distributed systems: [LEARN LATER] property validation is local to one object;
it does not replace validation at service or database boundaries.
"""


# ================================================================
# 15. IMPORTANT TECHNIQUES TO RECOGNIZE
# ================================================================
"""
Technique                    This chapter's connection
@property                   method accessed with attribute syntax
@name.setter                validate assignments to a property
@name.deleter               control deletion with del
_backing_attribute          store the actual value safely
computed attribute          derive a value from current object state
super().property            extend an inherited property
hasattr/getattr             inspect optional properties safely
property object             [LEARN LATER] descriptor behind the decorator
data validation             [LEARN LATER] larger validation libraries later
"""


# ================================================================
# 16. MINI PRACTICE: DO THESE WITHOUT LOOKING AT A SOLUTION
# ================================================================
"""
1. Easy: Create a `Circle` class with a radius attribute and a read-only `area`
   property. Use 3.14 for pi.

2. Easy/Medium: Create a `User` class with an age property. Reject ages below
   0 or above 130 in the setter.

3. Medium: Create an `Invoice` class with quantity and unit_price. Add a
   read-only total property and a discount property with validation.

4. Tricky: Create a `Document` class with a text setter that strips whitespace
   and rejects empty text. Add a word_count property.

5. Interview-style: Decide whether each should be a property or method:
   - order.total;
   - order.cancel();
   - model.predict(input_data);
   - user.email validation;
   - client.refresh_token().
"""


# ================================================================
# 17. INTERVIEW / MIND-TWISTING QUESTIONS
# ================================================================
"""
Question 1 - Easy
What does @property change about how a method is called?

Question 2 - Easy output prediction
class User:
	def __init__(self, name):
		self.name = name

	@property
	def greeting(self):
		return "Hello " + self.name

print(User("Aisha").greeting)

Question 3 - Easy/Medium
Why do property setters commonly use a backing attribute such as _email?

Question 4 - Medium debugging
What is wrong with this setter?
@email.setter
def email(self, value):
	self.email = value

Question 5 - Medium output prediction
class Item:
	def __init__(self, price):
		self.price = price

	@property
	def total(self):
		return self.price * 2

item = Item(5)
item.price = 7
print(item.total)

Question 6 - Medium
When should you use a normal method instead of a property?

Question 7 - Tricky
Why is a database query usually a poor implementation for a property getter?

Question 8 - Tricky output prediction
class Parent:
	@property
	def label(self):
		return "parent"

class Child(Parent):
	@property
	def label(self):
		return super().label + " child"

print(Child().label)

Question 9 - Interview-style
Design an `Account.balance` property that prevents negative assignment but still
allows deposits and withdrawals through methods.
"""


# ================================================================
# 18. ANSWERS + EXPLANATIONS
# ================================================================
"""
1. @property lets callers use `obj.value` instead of `obj.value()`.

2. It prints `Hello Aisha`. Reading greeting runs the getter.

3. Writing self.email inside the setter would call the setter again. `_email`
   stores the actual value under a different name.

4. It recursively calls itself until Python raises RecursionError. Store the
   validated value in self._email instead.

5. It prints 14. The property calculates from the current price each time it is
   read, so changing price changes total.

6. Use a method for an action, when arguments are needed, or when the work may
   be expensive or have side effects.

7. Property access looks cheap and local. Hiding network or database I/O behind
   it can cause slow, surprising behavior in ordinary attribute reads.

8. It prints `parent child`. The child property extends the parent property
   with super().label.

9. Store the balance through a validated property setter, and let deposit and
   withdraw methods enforce the business rules for changes.
"""


# ================================================================
# 19. COMMON INTERVIEW TRAPS
# ================================================================
"""
- A property is accessed without parentheses.
- A setter must store to a different backing attribute to avoid recursion.
- A property without a setter is read-only through normal assignment.
- `_name` is a convention for internal use, not strict privacy.
- Getters should not hide expensive I/O or actions.
- Validation in a setter runs during construction if __init__ uses the property.
- Properties can be overridden just like normal methods.
- `hasattr()` may execute a property getter and can therefore trigger errors or
  work; use it thoughtfully.
- A property does not automatically make data immutable.
- A property is not always better than a simple attribute or method.
"""


# ================================================================
# 20. FUTURE ROADMAP CONNECTION
# ================================================================
"""
CURRENT CHAPTER: @property decorator
		↓
WHAT I LEARNED: controlled attribute access, validation, and computed values
		↓
WHERE IT APPEARS LATER: API models, database entities, configuration objects
		↓
BACKEND / AI APPLICATION: keep object state valid while exposing clean,
readable interfaces to services, data pipelines, and AI components.
"""


if __name__ == "__main__":
	assert person.fullname == "Dan Lee"
	assert user.email == "new@example.com"
	assert safe_name.name == "Aisha"
	assert order.total == 59.97
	assert product.price == 55.5
	assert not hasattr(temporary_token, "_token")
	assert temperature.fahrenheit == 32
	assert account.status == "premium healthy"
	assert config.effective_timeout == 5
	assert custom_config.effective_timeout == 20
	print("\nChapter checks passed.")
