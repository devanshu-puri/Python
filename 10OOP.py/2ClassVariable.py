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

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test' , 'User', 60000)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# print namespace 
# print(emp_1.__dict__)
# print(Employee.__dict__)

Employee.raise_amount = 1.06 #change raise_amount for class and instances

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

#if we did emp_1.raise_amount = 1.05 then it will change only for emp_1

#main differnce isntance variable and class vairable

# ================== Corey's python end ========================================


"""Chapter 2: Class variables.

Run this file with:
	python 10OOP.py/2ClassVariable.py

This chapter assumes you already know classes, __init__, self, methods, and
instance attributes from 1Classes_Instances.py.
"""


# ================================================================
# 1. CORE IDEA: INSTANCE VARIABLES VS CLASS VARIABLES
# ================================================================
# An instance variable belongs to one object.
# A class variable belongs to the class and is shared by instances when they
# do not have their own attribute with the same name.
class Employee:
	company = "Northwind"  # class variable
	employee_count = 0     # shared counter

	def __init__(self, name, role):
		self.name = name    # instance variable
		self.role = role    # instance variable
		Employee.employee_count += 1


employee1 = Employee("Aisha", "Backend Engineer")
employee2 = Employee("Daniel", "Data Engineer")

print("Employee 1:", employee1.name, employee1.role)
print("Employee 2:", employee2.name, employee2.role)
print("Shared company:", Employee.company)
print("Access through an instance:", employee1.company)
print("Number of employees:", Employee.employee_count)


# ================================================================
# 2. CLASS ATTRIBUTE LOOKUP
# ================================================================
class AppConfig:
	environment = "development"


config1 = AppConfig()
config2 = AppConfig()

print("\nClass lookup:", AppConfig.environment)
print("Instance lookup:", config1.environment)
print("Both instances see:", config1.environment == config2.environment)


# Python checks the instance first, then the class.
print("Before shadowing:", config1.environment)
config1.environment = "testing"
print("config1 after assignment:", config1.environment)
print("config2 is unchanged:", config2.environment)
print("The class is unchanged:", AppConfig.environment)


# ================================================================
# 3. REBINDING VS MUTATING A CLASS VARIABLE
# ================================================================
class FeatureFlags:
	enabled = {"search": True, "recommendations": False}


flags1 = FeatureFlags()
flags2 = FeatureFlags()

# Mutation changes the shared dictionary.
flags1.enabled["recommendations"] = True
print("\nShared after mutation:", flags2.enabled)

# Assignment creates an instance attribute and does not rebind the class.
flags1.enabled = {"search": False, "recommendations": False}
print("flags1 after assignment:", flags1.enabled)
print("flags2 still uses class data:", flags2.enabled)
print("Class value:", FeatureFlags.enabled)


# ================================================================
# 4. INTENTIONAL SHARED STATE: CLASS-LEVEL REGISTRY
# ================================================================
class Plugin:
	registry = []

	def __init__(self, name):
		self.name = name
		Plugin.registry.append(name)


Plugin("logging")
Plugin("metrics")
print("\nRegistered plugins:", Plugin.registry)

# A shared mutable class variable is appropriate here because one registry is
# intentionally shared by every Plugin object.


# ================================================================
# 5. CLASS VARIABLES AND INHERITANCE
# ================================================================
class Model:
	framework = "Python"


class TextModel(Model):
	pass


print("\nInherited class variable:", TextModel.framework)
Model.framework = "Python + NumPy"
print("Inherited update:", TextModel.framework)

# Assignment on the child creates an override on that child.
TextModel.framework = "Python + PyTorch"
print("Child override:", TextModel.framework)
print("Parent remains:", Model.framework)


# ================================================================
# 6. INSPECTING WHERE AN ATTRIBUTE LIVES
# ================================================================
class Service:
	timeout_seconds = 30

	def __init__(self, name):
		self.name = name


service = Service("users")
print("\nInstance attributes:", service.__dict__)
print("Class attributes defined here:", Service.__dict__["timeout_seconds"])
print("Has instance timeout?", "timeout_seconds" in service.__dict__)

service.timeout_seconds = 10
print("After shadowing:", service.__dict__)
del service.timeout_seconds
print("After deleting shadow: ", service.timeout_seconds)


# ================================================================
# 7. USEFUL BUILT-INS FOR ATTRIBUTE CHECKS
# ================================================================
print("\nHas service name:", hasattr(service, "name"))
print("Read timeout safely:", getattr(service, "timeout_seconds", 60))
setattr(service, "region", "eu-west-1")
print("Dynamic attribute:", service.region)


# ================================================================
# 8. COMMON CLASS-VARIABLE PATTERNS
# ================================================================
class ApiClient:
	default_timeout = 5
	user_agent = "learning-client/1.0"

	def __init__(self, timeout=None):
		self.timeout = (
			ApiClient.default_timeout if timeout is None else timeout
		)


client1 = ApiClient()
client2 = ApiClient(timeout=20)
print("\nDefault timeout:", client1.timeout)
print("Custom timeout:", client2.timeout)


class Request:
	created = 0

	def __init__(self, path):
		self.path = path
		type(self).created += 1


Request("/health")
Request("/users")
print("Requests created:", Request.created)


# ================================================================
# 9. MUST-KNOW SUMMARY
# ================================================================
print("\nMUST KNOW")
print("- Class variables are defined in the class body.")
print("- Use ClassName.attribute when you mean shared class state.")
print("- obj.attribute first checks the instance, then the class.")
print("- obj.attribute = value usually creates or changes instance state.")
print("- Mutable class variables are shared and can cause accidental leaks.")
print("- Use a class variable for constants or intentionally shared state.")


# ================================================================
# 10. COMMONLY SKIPPED DETAILS AND EDGE CASES
# ================================================================
"""
Common mistakes:
- Defining items = [] in the class when every object needs its own list.
- Writing obj.setting = value and expecting the class value to change.
- Assuming obj.attribute proves the attribute belongs to the instance.
- Comparing objects with `is` when you mean equal values with `==`.
- Modifying a shared collection without realizing every instance can see it.
- Using a mutable class variable for per-user, per-request, or per-record data.

Pythonic habits:
- Name constants in UPPER_CASE, such as DEFAULT_TIMEOUT = 5.
- Use ClassName.attribute when reading or changing shared state.
- Use None as a default and create a new list/dict inside __init__ for each object.
- Keep shared mutable state intentional and small.

[LEARN LATER] `@classmethod` receives `cls` and is useful for constructors or
operations that work with class state. The next chapter can cover it properly.

[LEARN LATER] `dataclasses` can generate __init__ and other methods for data
objects. They are useful later, but first understand normal attributes.
"""


# ================================================================
# 11. USED LATER GLIMPSE
# ================================================================
"""
Concept: class constants
Why it matters later: Shared defaults make configuration consistent.
Where: API clients, database settings, model configuration.

Concept: shared counters and registries
Why it matters later: Objects may need a simple process-local count or registry.
Where: tests, plugin systems, metrics, resource tracking.

Concept: attribute lookup and shadowing
Why it matters later: Configuration objects often combine defaults and overrides.
Where: FastAPI dependencies, service clients, model settings.

Concept: mutable versus immutable values
Why it matters later: Shared state can accidentally leak between requests or jobs.
Where: backend request handling, data processing, cached AI configuration.

Backend/API: a class can hold a default timeout or user-agent for clients.
Databases: repository objects may share immutable connection settings.
Data processing: pipeline classes may share a read-only schema or format name.
AI/ML: model classes may share a model name or default device setting.
RAG/LLM: retriever classes may share immutable defaults such as top_k.
Async/concurrency: shared mutable state needs extra care when many tasks run.
Distributed systems: class variables belong to one Python process, not every
server or worker. [LEARN LATER]
"""


# ================================================================
# 12. IMPORTANT TECHNIQUES TO RECOGNIZE
# ================================================================
"""
Technique                 This chapter's connection
attribute lookup          obj -> class when reading an attribute
hasattr/getattr           inspect or safely read optional attributes
setattr                   set an attribute from a dynamic name
__dict__                  inspect instance attributes while debugging
type(self)                update the class that created the current object
None defaults             create per-instance mutable values safely
truthiness                useful in later configuration checks
**kwargs / *args          [LEARN LATER] flexible constructors and APIs
comprehensions            [LEARN LATER] concise processing of registries
generators                [LEARN LATER] memory-efficient data pipelines
"""


# ================================================================
# 13. MINI PRACTICE: DO THESE WITHOUT LOOKING AT A SOLUTION
# ================================================================
"""
1. Easy: Create a `Book` class with a class variable `category = "technical"`
   and an instance variable `title`. Create two books and print both values.

2. Easy/Medium: Add a class variable `count` to a `User` class. Increment it
   in __init__ and print the count after creating three users.

3. Medium: Create a `Cart` class. Give each cart its own `items` list, then
   prove that adding to one cart does not change another cart.

4. Tricky: Create a class with a shared `tags` set. Mutate it through one
   object, then assign a new set through that object. Predict both outputs.

5. Interview-style: Create a parent class with `status = "new"` and a child
   class. Show the difference between changing the parent and overriding the
   child. Inspect __dict__ to explain the result.
"""


# ================================================================
# 14. INTERVIEW / MIND-TWISTING QUESTIONS
# ================================================================
"""
Question 1 - Easy
What is the difference between a class variable and an instance variable?

Question 2 - Easy output prediction
class A:
	value = 1
a = A()
b = A()
a.value = 2
print(A.value, a.value, b.value)

Question 3 - Medium output prediction
class Team:
	members = []
x = Team()
y = Team()
x.members.append("Sam")
print(y.members)
Why?

Question 4 - Medium debugging
Fix this design if every object should have a separate list:
class Pipeline:
	steps = []

Question 5 - Medium
Why is `ClassName.setting = value` clearer than `obj.setting = value`
when changing shared class state?

Question 6 - Tricky output prediction
class Parent:
	mode = "safe"
class Child(Parent):
	pass
Parent.mode = "fast"
Child.mode = "debug"
print(Parent.mode, Child.mode)

Question 7 - Tricky
After `obj.value = 99`, how can you check whether `value` is stored on the
instance or only found on the class?

Question 8 - Interview-style
Give one example where a mutable class variable is intentional and one where
it is a bug.
"""


# ================================================================
# 15. ANSWERS + EXPLANATIONS
# ================================================================
"""
1. A class variable is shared through the class; an instance variable belongs
   to one object. An instance can read an inherited class value until it gets
   an attribute with the same name.

2. `1 2 1`. Assignment through `a` creates an instance attribute and shadows
   the class value. `b` still finds the class value.

3. `['Sam']`. The list is one shared mutable object stored on `Team`.

4. Move `steps = []` into __init__:
   def __init__(self):
	   self.steps = []

5. It communicates intent: the class is being changed for every instance that
   has not overridden the attribute.

6. `fast debug`. The parent is changed to `fast`; the child then gets its own
   override, so it reports `debug`.

7. Check `"value" in obj.__dict__`. You can also inspect `type(obj).__dict__`
   for attributes defined directly on the class.

8. Intentional: a Plugin.registry collecting all registered plugin names.
   Bug: a User.preferences dictionary shared by every user.
"""


# ================================================================
# 16. FUTURE ROADMAP CONNECTION
# ================================================================
"""
CURRENT CHAPTER: Class variables
		↓
WHAT I LEARNED: shared state, lookup, shadowing, mutation, inheritance
		↓
WHERE IT APPEARS LATER: client defaults, registries, model configuration
		↓
BACKEND / AI APPLICATION: API services and AI pipelines use classes to group
configuration and behavior, while request-specific data stays per instance.
"""


if __name__ == "__main__":
	assert Employee.employee_count == 2
	assert config1.environment == "testing"
	assert config2.environment == "development"
	assert flags2.enabled["recommendations"] is True
	assert TextModel.framework == "Python + PyTorch"
	assert Model.framework == "Python + NumPy"
	assert service.timeout_seconds == Service.timeout_seconds
	print("\nChapter checks passed.")
