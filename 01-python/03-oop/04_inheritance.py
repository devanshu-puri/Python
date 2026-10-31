class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay): #email can be created from first and last
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last) 

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount) #or self.raise_amount)


# class Developer(Employee):
#     pass #even without any code this class has all instances and function

class Developer(Employee):
    raise_amount = 1.10
    def __init__(self, first, last, pay, pro_lang):
        super().__init__(first, last, pay)
        # alternate of upper line, Employee.__init__(self,first, last , pay)
        self.pro_lang = pro_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees= None):
            super().__init__(first, last, pay)
            # alternate of upper line, Employee.__init__(self,first, last , pay)
            if employees is None:
                self.semployees = []
            else:
                self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
            if emp in self.employees:
                self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('--->',emp.fullname())

dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test' , 'User', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 900000, [dev_1])

print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
mgr_1.print_emp()

# dev_1 = Employee('Corey', 'Schafer', 50000)
# dev_2 = Employee('Test' , 'User', 60000)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay) 

# print(dev_1.email)
# print(dev_1.pro_lang)

#to check the instance 
print(isinstance(mgr_1, Manager)) #true
print(isinstance(mgr_1, Employee)) #true
print(isinstance(mgr_1, Developer)) #Even though Developer and manager are inheritance from Employee they are not each other's inheritance

print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))

#=============================== Corey pyton End ===================================================================


"""Chapter 4: inheritance.

Run this file with:
	python 10OOP.py/4Inheritance.py

Prerequisite: classes, instance methods, class methods, static methods, and
class variables.
"""


# ================================================================
# 1. BASIC INHERITANCE: A CHILD REUSES A PARENT
# ================================================================
class Person:
	def __init__(self, name):
		self.name = name

	def introduce(self):
		return f"I am {self.name}."


class Engineer(Person):
	pass


engineer = Engineer("Aisha")
print("Inherited constructor:", engineer.name)
print("Inherited method:", engineer.introduce())
print("Is an Engineer a Person?", isinstance(engineer, Person))
print("Is an Engineer an Engineer?", isinstance(engineer, Engineer))
print("Is Person a subclass of Engineer?", issubclass(Person, Engineer))


# `class Child(Parent)` means Engineer inherits from Person.
# `pass` means the child adds no new behavior yet.


# ================================================================
# 2. EXTENDING A PARENT CLASS
# ================================================================
class BackendEngineer(Person):
	def __init__(self, name, framework):
		super().__init__(name)
		self.framework = framework

	def build_service(self):
		return f"{self.name} builds a {self.framework} service."


backend_engineer = BackendEngineer("Daniel", "FastAPI")
print("\nExtended child:", backend_engineer.introduce())
print("Child behavior:", backend_engineer.build_service())


# `super()` gives access to the parent implementation. This avoids copying
# the parent's initialization code into every child class.


# ================================================================
# 3. OVERRIDING A METHOD
# ================================================================
class Notification:
	def send(self, message):
		return f"Sending notification: {message}"


class EmailNotification(Notification):
	def send(self, message):
		return f"Sending email: {message}"


class SmsNotification(Notification):
	def send(self, message):
		return f"Sending SMS: {message}"


notifications = [
	Notification(),
	EmailNotification(),
	SmsNotification(),
]

print("\nOverridden methods:")
for item in notifications:
	print(item.send("Your report is ready"))


# The child method replaces the inherited method for that child. The method
# signature should remain compatible with the parent method when possible.


# ================================================================
# 4. OVERRIDE AND EXTEND WITH super()
# ================================================================
class BaseReport:
	def title(self):
		return "System report"


class SalesReport(BaseReport):
	def title(self):
		parent_title = super().title()
		return f"{parent_title} - sales"


print("\nOverride plus parent behavior:", SalesReport().title())


# Use super() when the child needs both the parent's behavior and its own.


# ================================================================
# 5. INHERITING AND EXTENDING __init__
# ================================================================
class Account:
	account_type = "standard"

	def __init__(self, owner, balance=0):
		self.owner = owner
		self.balance = balance

	def deposit(self, amount):
		if amount <= 0:
			raise ValueError("Deposit must be positive")
		self.balance += amount
		return self.balance


class BusinessAccount(Account):
	account_type = "business"

	def __init__(self, owner, balance=0, company_name=""):
		super().__init__(owner, balance)
		self.company_name = company_name


business_account = BusinessAccount("Northwind", 1000, "Northwind Labs")
business_account.deposit(250)
print("\nInherited account data:", business_account.owner, business_account.balance)
print("Child account data:", business_account.company_name)
print("Overridden class variable:", business_account.account_type)


# If the child defines __init__ without calling super().__init__, parent
# attributes such as owner and balance will not be created automatically.


# ================================================================
# 6. POLYMORPHISM: ONE INTERFACE, DIFFERENT BEHAVIOR
# ================================================================
class CsvExporter:
	def export(self, records):
		return "csv:" + str(len(records))


class JsonExporter:
	def export(self, records):
		return "json:" + str(len(records))


def export_records(exporter, records):
	return exporter.export(records)


records = [{"id": 1}, {"id": 2}]
print("\nPolymorphism:", export_records(CsvExporter(), records))
print("Polymorphism:", export_records(JsonExporter(), records))


# Python often uses duck typing: if an object has the needed export method,
# the function can use it without checking its exact class.


# ================================================================
# 7. DUCK TYPING WITHOUT INHERITANCE
# ================================================================
class FakeExporter:
	def export(self, records):
		return f"fake:{len(records)}"


print("Duck typing:", export_records(FakeExporter(), records))


# Shared behavior can be enough. Inheritance is not required merely because
# two unrelated classes happen to provide the same method.


# ================================================================
# 8. isinstance() AND issubclass()
# ================================================================
print("\nExporter is object:", isinstance(JsonExporter(), object))
print("JsonExporter is CsvExporter subclass:", issubclass(JsonExporter, CsvExporter))
print("BusinessAccount is Account subclass:", issubclass(BusinessAccount, Account))


# Use isinstance when you have an object. Use issubclass when you have a class.
# Avoid excessive type checks when a simple shared interface is sufficient.


# ================================================================
# 9. MULTI-LEVEL INHERITANCE
# ================================================================
class Device:
	def power_on(self):
		return "Device is on"


class Computer(Device):
	def run_program(self):
		return "Program is running"


class Laptop(Computer):
	def close_lid(self):
		return "Laptop lid closed"


laptop = Laptop()
print("\nMulti-level inheritance:", laptop.power_on())
print("Multi-level inheritance:", laptop.run_program())
print("Multi-level inheritance:", laptop.close_lid())


# Multi-level inheritance works, but long inheritance chains can become hard
# to understand. Keep the hierarchy small and meaningful.


# ================================================================
# 10. MULTIPLE INHERITANCE: SMALL, PRACTICAL EXAMPLE
# ================================================================
class JsonSerializable:
	def to_json_ready(self):
		return {"name": self.name}


class Loggable:
	def log_label(self):
		return f"object={type(self).__name__}"


class Service(JsonSerializable, Loggable):
	def __init__(self, name):
		self.name = name


service = Service("search")
print("\nMultiple inheritance:", service.to_json_ready())
print("Multiple inheritance:", service.log_label())
print("Method resolution order:", [cls.__name__ for cls in Service.__mro__])


# Multiple inheritance can combine small, focused capabilities. This pattern
# is often called using mixins. [LEARN LATER] Study MRO deeply later.


# ================================================================
# 11. ABSTRACT-STYLE BASE CLASS WITH NotImplementedError
# ================================================================
class Storage:
	def save(self, record):
		raise NotImplementedError("Child classes must implement save")


class InMemoryStorage(Storage):
	def __init__(self):
		self.records = []

	def save(self, record):
		self.records.append(record)
		return record


storage = InMemoryStorage()
storage.save({"id": 1})
print("\nStorage implementation:", storage.records)


# The base class defines the expected operation. Later, the real `abc` module
# can enforce abstract methods more formally. [LEARN LATER]


# ================================================================
# 12. COMPOSITION VS INHERITANCE
# ================================================================
class Logger:
	def write(self, message):
		return f"LOG: {message}"


class UserService:
	def __init__(self, logger):
		self.logger = logger

	def create_user(self, name):
		return self.logger.write(f"created user {name}")


user_service = UserService(Logger())
print("\nComposition:", user_service.create_user("Aisha"))


# Inheritance means "is a" (an EmailNotification is a Notification).
# Composition means "has a" (a UserService has a Logger).
# Backend code often favors composition when behavior should be replaceable.


# ================================================================
# 13. CLASS METHODS IN INHERITED CLASSES
# ================================================================
class Model:
	model_type = "base"

	@classmethod
	def create(cls):
		return cls()


class TextModel(Model):
	model_type = "text"


created_model = TextModel.create()
print("\nInherited class method creates:", type(created_model).__name__)
print("Inherited class configuration:", created_model.model_type)


# This connects the previous chapter to inheritance: cls points to TextModel
# when the inherited class method is called through TextModel.


# ================================================================
# 14. COMMONLY SKIPPED DETAILS AND EDGE CASES
# ================================================================
"""
MUST KNOW:
- A child inherits accessible methods and attributes from its parent.
- A child can add new behavior or override existing behavior.
- super() calls the next implementation in the inheritance chain.
- __init__ is not automatically combined when a child defines its own __init__.
- Polymorphism lets one function work with different compatible objects.
- `isinstance(obj, Parent)` is true for a Parent object and its child objects.
- Composition is often clearer when a class simply needs another object.

Commonly skipped:
- `isinstance` includes inherited types; exact type checks are stricter.
- Class variables can be inherited and overridden by child classes.
- A parent method can be called explicitly, but super() is usually clearer.
- Multiple inheritance follows a method resolution order (MRO).
- A child override should preserve the parent's expected input/output contract.

Common mistakes:
- Forgetting super().__init__() and then accessing missing parent attributes.
- Copying parent code instead of reusing it with super().
- Making an inheritance relationship only because code looks similar.
- Building deep, fragile inheritance trees.
- Calling a child-only method on a variable that may only be a parent object.
- Changing a shared inherited class variable when an instance value was needed.
- Using isinstance checks everywhere instead of relying on a shared interface.

Pythonic habits:
- Keep parent classes small and focused.
- Prefer composition when a class has another component.
- Use duck typing when only a method contract matters.
- Use super() for cooperative initialization and extension.
- Name child classes after meaningful specializations.

[LEARN LATER] `abc.ABC` and `@abstractmethod` formalize required child methods.
Learn them after basic inheritance feels natural.

[LEARN LATER] MRO and cooperative multiple inheritance matter in framework code,
but you only need to recognize the pattern now.
"""


# ================================================================
# 15. USED LATER GLIMPSE
# ================================================================
"""
Concept: inheritance and overriding
Why it matters later: specialized services can share a common interface.
Where: exporters, storage adapters, authentication providers, model loaders.

Concept: super()
Why it matters later: child classes can extend shared setup without duplication.
Where: service configuration, request clients, data models.

Concept: polymorphism and duck typing
Why it matters later: pipeline functions can accept interchangeable components.
Where: FastAPI dependencies, database backends, serializers, AI retrievers.

Concept: composition
Why it matters later: replaceable collaborators make backend code easier to test.
Where: services with loggers, repositories, HTTP clients, or model providers.

Concept: base contracts
Why it matters later: different implementations can follow the same operation.
Where: database storage, caching, vector search, file storage, model inference.

Backend/FastAPI: different notification or storage implementations can expose
the same methods while the route/service code stays simple.
Databases: repository implementations may share a base interface while using
different database engines.
Data processing: exporters and parsers can be swapped in a pipeline.
AI/ML: model or embedding providers can share a small interface.
RAG/LLM: retrievers and vector stores may be interchangeable components.
Async/concurrent: [LEARN LATER] async child methods must preserve compatible
async behavior; do not mix sync and async methods casually.
Distributed systems: [LEARN LATER] inheritance organizes local code, but it
does not make objects or state shared between processes or machines.
"""


# ================================================================
# 16. IMPORTANT TECHNIQUES TO RECOGNIZE
# ================================================================
"""
Technique                    This chapter's connection
class Child(Parent)          declares inheritance
super()                      reuse the next parent implementation
method overriding            specialize inherited behavior
isinstance / issubclass      inspect object/class relationships
duck typing                  use required behavior, not exact type
polymorphism                 one call shape, different implementations
multiple inheritance         combine focused mixin capabilities
__mro__                      inspect method lookup order
NotImplementedError          basic base-class contract
composition                  has-a relationship with another object
abc module                   [LEARN LATER] formal abstract interfaces
"""


# ================================================================
# 17. MINI PRACTICE: DO THESE WITHOUT LOOKING AT A SOLUTION
# ================================================================
"""
1. Easy: Create a `Vehicle` parent with a `start` method. Create a `Car` child
   that inherits and uses the method.

2. Easy/Medium: Create an `Employee` parent with name initialization. Create a
   `Manager` child with a team_size field using super().__init__.

3. Medium: Create `PdfReport` and `HtmlReport` classes with the same `render`
   method. Write one function that renders either object polymorphically.

4. Tricky: Create a `FileStorage` base class with `save`. Implement an
   `InMemoryStorage` child and raise NotImplementedError in the base method.

5. Interview-style: Build a `SearchService` using composition with a `Logger`
   and a `Repository`. Replace the repository with a fake object in a test.
"""


# ================================================================
# 18. INTERVIEW / MIND-TWISTING QUESTIONS
# ================================================================
"""
Question 1 - Easy
What does `class Child(Parent)` mean?

Question 2 - Easy output prediction
class A:
	def speak(self):
		return "A"

class B(A):
	pass

print(B().speak())

Question 3 - Easy/Medium
Why do we call `super().__init__()` in a child constructor?

Question 4 - Medium output prediction
class Parent:
	value = "parent"

class Child(Parent):
	value = "child"

print(Child.value, Parent.value)

Question 5 - Medium debugging
What is missing here?
class Child(Parent):
	def __init__(self, name, role):
		self.role = role

Question 6 - Medium
Explain the difference between inheritance and composition using "is-a" and
"has-a" examples.

Question 7 - Tricky output prediction
class A:
	def run(self):
		return "A"

class B(A):
	def run(self):
		return super().run() + "B"

print(B().run())

Question 8 - Tricky
Why can duck typing reduce the need for isinstance checks?

Question 9 - Interview-style
When should you avoid inheritance even if two classes share some code?
"""


# ================================================================
# 19. ANSWERS + EXPLANATIONS
# ================================================================
"""
1. Child inherits accessible behavior and attributes from Parent and may add or
   override behavior.

2. It prints A because B inherits speak unchanged.

3. The parent constructor creates the parent part of the child object, such as
   name or other required attributes.

4. It prints `child parent`. The child overrides the inherited class variable;
   the parent class remains unchanged.

5. The child never calls super().__init__(name), so the parent attributes are
   not initialized. Add the super call before setting role.

6. Inheritance is an "is-a" relationship: a Manager is an Employee.
   Composition is a "has-a" relationship: a Service has a Repository.

7. It prints AB. super().run() returns A, then B appends its own behavior.

8. If an object provides the method the function needs, its concrete class is
   often irrelevant. This keeps code flexible and reduces coupling.

9. Avoid it when the relationship is not truly is-a, when the hierarchy becomes
   deep, or when composition makes the dependency easier to replace and test.
"""


# ================================================================
# 20. COMMON INTERVIEW TRAPS
# ================================================================
"""
- Defining a child __init__ does not automatically call the parent __init__.
- `super()` is not the same as calling a hard-coded parent class; it respects
  the inheritance order.
- `isinstance(child, Parent)` can be True even when type(child) is not Parent.
- A class variable inherited by a child may be overridden on the child.
- Overriding a method with an incompatible signature can break callers.
- Similar code does not always mean inheritance is the right relationship.
- Duck typing can work without a shared parent class.
- Multiple inheritance can make method lookup surprising; keep mixins small.
- NotImplementedError is a runtime signal, not the same as @abstractmethod.
"""


# ================================================================
# 21. FUTURE ROADMAP CONNECTION
# ================================================================
"""
CURRENT CHAPTER: Inheritance
		↓
WHAT I LEARNED: reuse, overriding, super(), polymorphism, composition
		↓
WHERE IT APPEARS LATER: services, repositories, exporters, model providers
		↓
BACKEND / AI APPLICATION: interchangeable components can share small
interfaces while implementations vary for APIs, databases, and AI pipelines.
"""


if __name__ == "__main__":
	assert engineer.introduce() == "I am Aisha."
	assert backend_engineer.build_service() == "Daniel builds a FastAPI service."
	assert EmailNotification().send("hello") == "Sending email: hello"
	assert business_account.balance == 1250
	assert export_records(CsvExporter(), records) == "csv:2"
	assert export_records(FakeExporter(), records) == "fake:2"
	assert isinstance(business_account, Account)
	assert issubclass(BusinessAccount, Account)
	assert laptop.close_lid() == "Laptop lid closed"
	assert storage.records == [{"id": 1}]
	assert user_service.create_user("Daniel") == "LOG: created user Daniel"
	assert type(TextModel.create()).__name__ == "TextModel"
	print("\nChapter checks passed.")
