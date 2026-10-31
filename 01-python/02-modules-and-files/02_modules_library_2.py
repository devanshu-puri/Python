print("\n=== MODULES AND THE PYTHON STANDARD LIBRARY ===")

# A module is a Python file that contains reusable code.
# my_module.py is a local module in this same folder.
import my_module

courses = ['History', 'Math', 'Physics', 'CompSci']
index = my_module.find_index(courses, 'Math')
print('Math index:', index)
print('module value:', my_module.test)

# An import runs a module once and gives access through its module name.
print('missing course index:', my_module.find_index(courses, 'Biology'))

# An alias is useful when a module name is long or could be confused with a variable.
import my_module as mm

print('alias index:', mm.find_index(courses, 'Physics'))

# Import only the names that you need from a module.
from my_module import find_index

print('direct import index:', find_index(courses, 'CompSci'))

# This is valid, but wildcard imports make it unclear where names came from.
# Avoid: from my_module import *

# Standard-library modules are included with Python; no pip install is needed.
import math
import random
import statistics

print('square root:', math.sqrt(25))
print('rounded up:', math.ceil(4.2))
print('rounded down:', math.floor(4.8))

random.seed(7)
print('random integer:', random.randint(1, 10))
print('average:', statistics.mean([10, 20, 30]))

# Import a specific function with an alias when that improves readability.
from pathlib import Path

current_file = Path(__file__)
print('file name:', current_file.name)
print('file suffix:', current_file.suffix)
print('file exists:', current_file.exists())

# pathlib is preferred over manually building OS-specific path strings.
lesson_folder = current_file.parent
helper_file = lesson_folder / 'my_module.py'
print('helper exists:', helper_file.exists())

# The datetime module is useful for timestamps and date calculations.
from datetime import date, timedelta

today = date.today()
tomorrow = today + timedelta(days=1)
print('today:', today)
print('tomorrow:', tomorrow)

# Importing a module creates a module object.
print('module name:', my_module.__name__)
print('module file:', my_module.__file__)

# dir() shows names available on a module. Filter it when exploring.
public_names = [name for name in dir(my_module) if not name.startswith('_')]
print('public names:', public_names)

# help() can show documentation interactively; __doc__ reads a docstring directly.
print('find_index documentation:', find_index.__doc__)

# A module can contain constants, functions, and classes together.
print('module attributes can be reused:', mm.test)

# Put reusable behavior in a function instead of running it at import time.
def find_course_index(course_name):
	return my_module.find_index(courses, course_name)


print('function using module:', find_course_index('History'))

# A module can be used by another module without copying its code.
def make_course_report(course_names):
	report = {}
	for course_name in course_names:
		report[course_name] = my_module.find_index(course_names, course_name)
	return report


print('course report:', make_course_report(courses))

# Import aliases do not copy the function; both names refer to the same function.
print('same function object:', find_index is my_module.find_index)

# A module import is normally cached in sys.modules after the first import.
import sys

print('module is cached:', 'my_module' in sys.modules)

# Importing the same module again reuses the cached module object.
import my_module as cached_module

print('same module object:', cached_module is my_module)

# json converts between Python data and JSON text, common in APIs.
import json

user = {'name': 'Ava', 'roles': ['backend', 'ai'], 'active': True}
json_text = json.dumps(user)
decoded_user = json.loads(json_text)
print('json text:', json_text)
print('decoded user:', decoded_user)

# [LEARN LATER] Reading and writing files with a module is important in real apps.
# This example only reads metadata, so it has no side effects.
print('helper size:', helper_file.stat().st_size, 'bytes')

# [LEARN LATER] Environment variables are commonly read with os or os.environ.
# Do not put passwords or API keys directly in source code.
import os

print('current folder:', os.getcwd())
print('optional setting:', os.environ.get('APP_MODE', 'development'))

# Module names are looked up using Python's import search path.
print('first import path entry:', sys.path[0])

# When this file is imported, the guarded code below does not run.
def main():
	print('main function called')


if __name__ == '__main__':
	main()


print("\n=== CHAPTER CHECK ===")
print('MUST KNOW: module files, import, aliases, selective imports, and module attributes')
print('COMMONLY SKIPPED: sys.path, import caching, __name__, __file__, and wildcard-import problems')
print('IMPORTANT OPERATIONS: dir(), help(), pathlib.Path, json.dumps(), json.loads(), and os.environ.get()')
print('COMMON PATTERN: keep reusable code in modules and execute demo code under an __main__ guard')
print('EDGE CASE: an import fails when Python cannot find the module on its import search path')
print('PYTHONIC: prefer explicit imports, pathlib paths, small modules, and clear module names')


print("\n=== USED LATER: SHORT GLIMPSES ===")
print('Modules -> Backend: separate routes, services, database code, and configuration.')
print('Modules -> FastAPI: endpoints are commonly organized across router modules.')
print('Modules -> Databases: connection helpers and query functions live in dedicated modules.')
print('Modules -> AI/ML: preprocessing, model loading, inference, and evaluation can be separated.')
print('Modules -> Data processing: reusable cleaning functions can be imported into jobs.')
print('Modules -> RAG/LLM: loaders, chunkers, retrievers, prompts, and evaluators often have modules.')
print('JSON -> APIs: request and response data are commonly represented as JSON.')
print('pathlib -> Backend/data: files, uploads, model artifacts, and logs need reliable paths.')
print('os.environ -> Production: configuration and secrets are supplied outside source code. [LEARN LATER]')
print('sys.path -> Debugging: import errors often depend on the current working directory. [LEARN LATER]')
print('Import caching -> Applications: modules are usually initialized once per Python process. [LEARN LATER]')


print("\n=== IMPORTANT TECHNIQUES ===")
print('Use import module when you want clear ownership, such as json.loads().')
print('Use from module import name for a small, obvious set of names.')
print('Use as aliases to avoid long names or naming conflicts.')
print('Avoid wildcard imports because they hide where names came from.')
print('Use __name__ == __main__ to separate reusable code from direct execution.')
print('Use pathlib.Path for paths instead of string concatenation.')
print('Use json.dumps/loads for Python value <-> JSON text conversion.')
print('Use json.dump/load when working directly with a file. [LEARN LATER]')
print('Use packages to organize related modules. [LEARN LATER]')
print('Use virtual environments and pip for third-party libraries. [LEARN LATER]')


print("\n=== INTERVIEW QUESTIONS ===")
print('1 EASY: What is a module in Python?')
print('2 EASY: What is the difference between import my_module and from my_module import find_index?')
print('3 EASY: What does import my_module as mm change?')
print('4 MEDIUM: Why is from my_module import * usually discouraged?')
print('5 MEDIUM: What does if __name__ == __main__ protect?')
print('6 MEDIUM: Why might import my_module work from one folder but fail from another?')
print('7 MEDIUM: What is the difference between json.dumps() and json.loads()?')
print('8 TRICKY: What does this print?')
print("   import my_module\n   import my_module as mm\n   print(my_module is mm)")
print('9 TRICKY: Write a module import that gives direct access to find_index but not the module name.')


print("\n=== ANSWERS + EXPLANATIONS ===")
print('1: A module is a .py file containing reusable Python code.')
print('2: import keeps access through my_module; from imports find_index directly into the current namespace.')
print('3: It gives my_module the shorter local name mm.')
print('4: It can overwrite existing names and makes code ownership unclear.')
print('5: It runs code only when the file is executed directly, not when imported.')
print('6: Python searches specific locations in sys.path, including locations affected by the working directory.')
print('7: dumps converts a Python object to JSON text; loads converts JSON text back to a Python object.')
print('8: True, because both names refer to the cached module object.')
print('9: from my_module import find_index')


print("\n=== COMMON INTERVIEW TRAPS ===")
print('A file name must match the import name; spelling mistakes cause ModuleNotFoundError.')
print('The current working directory and the script directory are related to import lookup but are not always identical.')
print('Do not name your file json.py, random.py, or pathlib.py; it can shadow a standard-library module.')
print('from module import name does not make a separate copy of the function.')
print('Importing a module can execute its top-level code, so keep side effects limited.')
print('__name__ is __main__ only when that file is run directly.')
print('JSON is text/data format, not the same thing as a Python dictionary.')
print('Third-party packages need installation; standard-library modules do not.')


print("\n=== MINI PRACTICE ===")
print('1 EASY: Import the math module and print the square root of 144.')
print('2 EASY/MEDIUM: Import find_index directly and find the index of a course.')
print('3 MEDIUM: Convert a dictionary to JSON text and back using dumps and loads.')
print('4 TRICKY: Create a function that accepts a file name and returns a Path with a logs/ folder.')
print('5 INTERVIEW: Create a small helper module with a function, then import it using a module alias.')


print("\n=== FUTURE ROADMAP ===")
print('Modules')
print('  -> reusable code and explicit imports')
print('  -> packages for backend, database, and AI components')
print('  -> JSON and pathlib for APIs and data workflows')
print('  -> FastAPI services, RAG pipelines, and production Python')


print("\n=== FINAL CHECKLIST ===")
print('MUST KNOW: modules, import, aliases, selective imports, standard library, and __main__')
print('GOOD TO KNOW: dir(), __file__, sys.path, import caching, pathlib, and JSON conversion')
print('LEARN LATER: packages, virtual environments, pip, relative imports, and plugin loading')
print('USED IN BACKEND: routers, services, repositories, configuration, and utility modules')
print('USED IN AI ENGINEERING: loaders, preprocessing, models, retrieval, prompts, and evaluation')
print('INTERVIEW IMPORTANT: import lookup, wildcard imports, shadowing, JSON, and __name__')
