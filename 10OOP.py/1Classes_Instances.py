# class Employee:
#     pass  #if want to keep class empty just write pass

# # each of these are unique instances of same class
# emp_1 = Employee()
# emp_2 = Employee()

#instance variable : 
#class variable : 

# emp_1.first = 'Corey'
# emp_1.last = 'Schafer'
# emp_1.email = 'Corey.Schafer@gmail.com'
# emp_1.pay = 50000

# emp_2.first = 'Test'
# emp_2.last = 'User'
# emp_2.email = 'Test.User@gmail.com'
# emp_2.pay = 60000

# print(emp_1.email)
# print(emp_2.email)

#instead of doing these manually evertime we set special init method

class Employee:
    def __init__(self, first, last, pay): #email can be created from first and last
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test' , 'User', 60000)

# print(emp_1.email)
# print(emp_2.email)

print(emp_1.fullname())

#they both do the same
print(emp_1.fullname())
print(Employee.fullname(emp_1))

#================== COrey's end ==========================


"""
Classes and Instances - Python OOP fundamentals

This file is a chapter practice file for learning:
- class vs instance
- __init__ and self
- instance attributes
- class attributes
- methods
- object identity and comparison
- common beginner mistakes

Run this file with:
    python 10OOP.py/1Classes_Instances.py
"""

# =========================
# 1) BASIC CLASS AND INSTANCE
# =========================
class Person:
    def greet(self):
        print("Hello! I am a Person.")

p1 = Person()
p2 = Person()

print("p1 is Person:", isinstance(p1, Person))
print("p2 is Person:", isinstance(p2, Person))
p1.greet()
p2.greet()


# =========================
# 2) __init__ and instance attributes
# =========================
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        return f"Hi, I am {self.name} and I am {self.age} years old."

student1 = Student("Aisha", 21)
student2 = Student("Daniel", 24)

print(student1.intro())
print(student2.intro())

print("student1.name ->", student1.name)
print("student2.age ->", student2.age)


# =========================
# 3) CLASS ATTRIBUTES VS INSTANCE ATTRIBUTES
# =========================
class Dog:
    species = "Canis familiaris"  # class attribute

    def __init__(self, name):
        self.name = name  # instance attribute

    def bark(self):
        return f"{self.name} says woof!"

my_dog = Dog("Bruno")
print("Class attribute:", Dog.species)
print("Instance attribute:", my_dog.name)
print(my_dog.bark())

# Changing instance attribute does not affect the class
my_dog.name = "Max"
print("After rename:", my_dog.name)
print("Class remains:", Dog.species)

# Changing class attribute affects all instances unless overridden
Dog.species = "Canis lupus familiaris"
print("Updated class attribute:", my_dog.species)


# =========================
# 4) METHODS THAT USE self
# =========================
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Not enough funds"
        self.balance -= amount
        return self.balance

account = BankAccount(100)
print("Initial balance:", account.balance)
print("Deposit:", account.deposit(50))
print("Withdraw:", account.withdraw(30))
print("Final balance:", account.balance)


# =========================
# 5) DEFAULT VALUES AND MUTABLE OBJECTS (important edge case)
# =========================
class ShoppingCart:
    def __init__(self, items=None):
        if items is None:
            self.items = []
        else:
            self.items = items

    def add_item(self, item):
        self.items.append(item)

cart1 = ShoppingCart()
cart2 = ShoppingCart()

cart1.add_item("apple")
print("cart1:", cart1.items)
print("cart2:", cart2.items)

# Why this matters: default None is safer than a mutable default list


# =========================
# 6) COMPARISON: == vs is
# =========================
class Book:
    def __init__(self, title):
        self.title = title

b1 = Book("Python Basics")
b2 = Book("Python Basics")
print("b1 == b2:", b1 == b2)  # compares object values only if __eq__ is defined
print("b1 is b2:", b1 is b2)  # identity check

# Very important concept: same value does not mean same object

# Strings are a special case in Python
s1 = "hello"
s2 = "hello"
print("s1 == s2:", s1 == s2)
print("s1 is s2:", s1 is s2)


# =========================
# 7) METHODS RETURNING A VALUE
# =========================
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

r = Rectangle(5, 3)
print("Area:", r.area())


# =========================
# 8) OBJECTS ARE REFERENCE TYPES
# =========================
class Profile:
    def __init__(self, name):
        self.name = name

p1 = Profile("Alice")
p2 = p1

p2.name = "Bob"
print("p1.name:", p1.name)
print("p2.name:", p2.name)

print("p1 is p2:", p1 is p2)


# =========================
# 9) A SMALL REAL-WORLD EXAMPLE: user record
# =========================
class User:
    def __init__(self, username, email, role="member"):
        self.username = username
        self.email = email
        self.role = role

    def profile(self):
        return {
            "username": self.username,
            "email": self.email,
            "role": self.role,
        }

user = User("alice_dev", "alice@example.com", "admin")
print(user.profile())


# =========================
# 10) COMMON MISTAKES DEMO
# =========================
class Counter:
    count = 0  # class attribute

    def __init__(self):
        self.count += 1  # this creates an instance attribute, not class update

# This may surprise beginners
c1 = Counter()
c2 = Counter()
print("c1.count:", c1.count)
print("c2.count:", c2.count)
print("Counter.count:", Counter.count)


# =========================
# 11) QUICK REVIEW
# =========================
print("\nQuick summary:")
print("- A class is a blueprint")
print("- An instance is a concrete object created from that class")
print("- __init__ runs when an instance is created")
print("- self points to the current instance")
print("- instance attributes are unique to each object")
print("- class attributes are shared across all instances")
print("- methods let objects perform actions")


# =========================
# 12) IF YOU WANT TO TEST IDEAS QUICKLY
# =========================
# You can create objects like this:
# person = Person()
# person.name = "Sam"
# person.say_hello = lambda: print("Hi")
# These are valid, but not the cleanest beginner pattern.
