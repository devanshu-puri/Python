def hello_func(greeting):
    return '{} funciton.'.format(greeting)

print(hello_func("HI"))

def hello_func2(greeting, name):
    return '{}, {}'.format(greeting, name)

print(hello_func2("hi", "devanshu"))

def student_info(*args, **kwargs): #when dont know how many position argument to be used.
    print(args)    
    print(kwargs)

student_info('Math', 'Art', name='John', age=22) #math, art positional argument, 
                                                #name, age are keyword argument

# if we do
# def student_info...
#but
courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info(courses, info) #this will pack them together

#to get unpacked version 
student_info(*courses, **info)

print("-----corey's part end--------")

print("\n=== FUNCTIONS ===")

# A function groups a reusable piece of work.
def greet():
	print('Hello, Python')


greet()

# Parameters receive input; arguments are the values passed by the caller.
def greet_user(name):
	print('Hello,', name)


greet_user('Ava')
greet_user('Sam')

# return sends a value back to the caller. It does not print automatically.
def add(first_number, second_number):
	return first_number + second_number


total = add(10, 5)
print('total:', total)

# A function without return returns None.
def log_message(message):
	print('LOG:', message)


result = log_message('request received')
print('returned value:', result)

# Parameters can have default values.
def connect(host, port=5432):
	return f'Connecting to {host}:{port}'


print(connect('localhost'))
print(connect('localhost', 6432))

# Positional arguments follow the parameter order.
print(add(2, 3))

# Keyword arguments make the meaning of values clear.
print(connect(host='database.internal', port=5432))

# Do not use a mutable object such as [] as a default value.
# Use None and create a new list inside the function instead.
def add_tag(tag, tags=None):
	if tags is None:
		tags = []
	tags.append(tag)
	return tags


print(add_tag('python'))
print(add_tag('backend'))

# Functions can accept more positional arguments with *args.
def total_price(*prices):
	return sum(prices)


print('price total:', total_price(12.50, 8.00, 5.50))

# *args is a tuple inside the function.
def show_arguments(*values):
	print('values:', values)


show_arguments('Python', 3, True)

# Functions can accept more keyword arguments with **kwargs.
def make_user(**fields):
	return fields


print(make_user(name='Ava', role='backend'))

# **kwargs is a dictionary inside the function.
def print_settings(**settings):
	for key, value in settings.items():
		print(key, '=', value)


print_settings(debug=True, timeout=30)

# * and ** also unpack an existing collection when calling a function.
numbers = [4, 6]
print(add(*numbers))

user_fields = {'name': 'Mia', 'role': 'ai'}
print(make_user(**user_fields))

# A function can combine normal, *args, and **kwargs parameters.
def request_summary(method, path, *tags, **metadata):
	return {
		'method': method,
		'path': path,
		'tags': tags,
		'metadata': metadata
	}


print(request_summary('GET', '/users', 'public', status=200))

# A keyword-only parameter comes after *.
def create_connection(host, *, secure=True, timeout=10):
	protocol = 'https' if secure else 'http'
	return f'{protocol}://{host} (timeout={timeout})'


print(create_connection('api.example.com', timeout=5))

# This would be an error because secure must be passed by name:
# create_connection('api.example.com', False, 5)

# A function can return multiple values. Python packs them into a tuple.
def min_max(values):
	return min(values), max(values)


smallest, largest = min_max([8, 3, 10, 2])
print('range:', smallest, largest)

# Unpacking makes multiple returned values easy to use.
first, second = ('first', 'second')
print(first, second)

# A docstring documents the purpose and contract of a function.
def percentage(part, whole):
	"""Return part as a percentage of whole."""
	if whole == 0:
		raise ValueError('whole must not be zero')
	return part / whole * 100


print('percentage:', percentage(25, 50))
print(percentage.__doc__)

# Type annotations describe expected types; Python does not enforce them here.
def format_user(name: str, active: bool = True) -> str:
	status = 'active' if active else 'inactive'
	return f'{name} ({status})'


print(format_user('Ava'))
print(format_user('Sam', active=False))

# Scope: local variables exist inside the function.
service_name = 'user-service'


def show_service():
	local_message = 'handling request'
	print(service_name, local_message)


show_service()
# local_message cannot be used here because it is local to show_service.

# Prefer returning a new value instead of changing global state.
request_count = 0


def count_request(current_count):
	return current_count + 1


request_count = count_request(request_count)
print('requests:', request_count)

# Arguments are passed by object reference: mutable objects can be changed in place.
def add_item(items, item):
	items.append(item)


items = ['book']
add_item(items, 'pen')
print('changed list:', items)

# Rebinding a parameter does not replace the caller's variable.
def replace_list(items):
	items = ['new value']


items = ['original']
replace_list(items)
print('after rebinding:', items)

# Keep functions focused: validate, transform, or coordinate one clear operation.
def normalize_username(username):
	return username.strip().lower()


print(normalize_username('  Ava_Dev  '))

# Guard clauses handle invalid cases early and keep the main path clear.
def get_display_name(user):
	if user is None:
		return 'Anonymous'
	if not user.get('name'):
		return 'Unnamed user'
	return user['name'].strip()


print(get_display_name(None))
print(get_display_name({'name': 'Mia'}))

# Functions are objects: they can be stored and passed to other functions.
def double(number):
	return number * 2


operation = double
print('stored function:', operation(6))


def apply_operation(operation, value):
	return operation(value)


print('callback result:', apply_operation(double, 7))

# A small lambda is sometimes useful as a one-expression function.
print('lambda result:', apply_operation(lambda number: number + 1, 7))

# sorted(key=...) receives a function that extracts the comparison value.
users = [
	{'name': 'Mia', 'score': 91},
	{'name': 'Ava', 'score': 84},
	{'name': 'Sam', 'score': 97},
]

ranked_users = sorted(users, key=lambda user: user['score'], reverse=True)
print('ranked:', ranked_users)

# Comprehensions are often clearer than map/filter for simple transformations.
scores = [72, 88, 95, 61]
passed_scores = [score for score in scores if score >= 70]
score_labels = [f'{score}%' for score in scores]
print('passed:', passed_scores)
print('labels:', score_labels)

# any() and all() pair naturally with generator expressions.
print('any high score:', any(score >= 90 for score in scores))
print('all passing:', all(score >= 60 for score in scores))

# Recursion means a function calls itself. Recognize it, but iterative code is
# usually easier to maintain at this stage.
def countdown(number):
	if number <= 0:
		return
	print(number)
	countdown(number - 1)


countdown(3)


def safe_percentage(part, whole):
	try:
		return percentage(part, whole)
	except ValueError as error:
		return f'Invalid input: {error}'


print(safe_percentage(1, 0))

# [LEARN LATER] A generator uses yield to produce values lazily.
def read_numbers(limit):
	for number in range(limit):
		yield number


print('generator values:', list(read_numbers(3)))

# [LEARN LATER] Decorators wrap a function to add reusable behavior.
def announce(function):
	def wrapper():
		print('starting function')
		return function()
	return wrapper


@announce
def load_config():
	return 'config loaded'


print(load_config())

# [LEARN LATER] async def defines a coroutine for asynchronous workflows.
# It is not run here because async programming belongs to a later chapter.


print("\n=== CHAPTER CHECK ===")
print('MUST KNOW: define, call, parameters, arguments, return, scope, and defaults')
print('COMMONLY SKIPPED: keyword arguments, unpacking, None defaults, mutation, and annotations')
print('PYTHONIC: small focused functions, guard clauses, comprehensions, any/all, and key=')
print('EDGE CASES: missing return gives None; zero division needs validation; mutable inputs can change')
print('COMMON MISTAKES: confusing print with return, using mutable defaults, and mixing positional order')


print("\n=== USED LATER: SHORT GLIMPSES ===")
print('Functions -> Backend: route handlers, validation helpers, and service functions.')
print('Functions -> FastAPI: endpoint functions receive request data and return responses.')
print('Functions -> Databases: repository functions hide query and connection details.')
print('Functions -> Data processing: transformation functions clean each record or batch.')
print('Functions -> AI/ML: preprocessing, prediction, evaluation, and pipeline steps are functions.')
print('Functions -> RAG/LLM: retrieval, chunking, prompt creation, and answer parsing are functions.')
print('Functions -> Async: async functions let I/O work be awaited later. [LEARN LATER]')
print('Functions -> Distributed systems: small functions become tasks or worker operations. [LEARN LATER]')
print('Callbacks -> Backend/AI: libraries call your function when an event or result is ready.')
print('Generators -> Data/RAG: large streams can be processed without loading everything at once. [LEARN LATER]')
print('Decorators -> Backend: authentication, logging, and timing can wrap functions. [LEARN LATER]')


print("\n=== IMPORTANT TECHNIQUES ===")
print('Learn now: return values, keyword arguments, unpacking, scope, mutation, and truthiness.')
print('Learn now: enumerate(), zip(), comprehensions, any(), all(), sorted(key=...), and lambda.')
print('Recognize this pattern: *args and **kwargs make reusable APIs flexible.')
print('Recognize this pattern: annotations document contracts and help tools find mistakes.')
print('Recognize this pattern: generators, decorators, closures, and async functions are later topics.')
print('Recognize this pattern: map/filter/reduce exist, but comprehensions are often clearer for simple work.')


print("\n=== INTERVIEW QUESTIONS ===")
print('1 EASY: What is the difference between print() and return?')
print('2 EASY: What value does a function return when it has no return statement?')
print('3 EASY: Write a function is_even(number) that returns True for even numbers.')
print('4 MEDIUM: What does this print?')
print("   def add_tag(tag, tags=[]):\n       tags.append(tag)\n       return tags\n   print(add_tag('a'))\n   print(add_tag('b'))")
print('5 MEDIUM: Why does changing a list inside a function affect the caller, but rebinding the parameter does not?')
print('6 MEDIUM: Write a function that accepts any number of scores and returns the average.')
print('7 TRICKY: What is returned by percentage(10, 0), and how should production code handle it?')
print('8 TRICKY: Predict the result of apply_operation(lambda value: value * 3, 4).')
print('9 INTERVIEW: Design a function with a required host and keyword-only timeout parameter.')


print("\n=== ANSWERS + EXPLANATIONS ===")
print('1: print displays a value; return sends a value to the caller.')
print('2: None. This is different from returning 0, False, or an empty string.')
print('3: return number % 2 == 0')
print('4: It prints [\'a\'] and then [\'a\', \'b\']; the same default list is reused.')
print('5: A mutable list can be changed in place; rebinding only changes the local parameter name.')
print('6: def average(*scores): return sum(scores) / len(scores)')
print('7: It raises ValueError from the validation in percentage; callers should validate or handle it.')
print('8: 12, because the lambda multiplies 4 by 3.')
print('9: def connect(host, *, timeout=10): return host, timeout')


print("\n=== COMMON INTERVIEW TRAPS ===")
print('Mutable default arguments keep state between calls; use None as the default.')
print('print() is not a substitute for return; returned values can be reused and tested.')
print('A missing return produces None, even if the function printed useful text.')
print('Mutating a list or dictionary argument is visible to the caller; rebinding is not.')
print('Positional arguments depend on order; keyword arguments depend on parameter names.')
print('Annotations are hints for readers and tools, not automatic runtime validation.')
print('A lambda should stay small; use def when the logic needs a name or explanation.')
print('Use is None for None checks; use == for value comparisons.')


print("\n=== MINI PRACTICE ===")
print('1 EASY: Write square(number) and return its square. Test it with 6.')
print('2 EASY/MEDIUM: Write clean_email(email) that strips spaces and lowercases the address.')
print('3 MEDIUM: Write total_cost(*prices) that returns the sum, then test three prices.')
print('4 TRICKY: Write add_unique(item, items=None) that returns a list with item added only once.')
print('5 INTERVIEW: Write summarize_users(users) that returns active users sorted by name.')


print("\n=== FUTURE ROADMAP ===")
print('Functions')
print('  -> reusable inputs, transformations, and outputs')
print('  -> backend handlers and database service functions')
print('  -> data processing and AI pipeline steps')
print('  -> FastAPI, RAG, and production Python')


print("\n=== FINAL CHECKLIST ===")
print('MUST KNOW: define/call, parameters, return, defaults, scope, mutation, and errors')
print('GOOD TO KNOW: *args, **kwargs, annotations, callbacks, comprehensions, and key=')
print('LEARN LATER: generators, decorators, closures, async functions, and reduce')
print('USED IN BACKEND: handlers, validators, services, repositories, and dependency functions')
print('USED IN AI ENGINEERING: preprocessing, inference, evaluation, retrieval, and prompt steps')
print('INTERVIEW IMPORTANT: return vs print, mutable defaults, scope, mutation, and unpacking')
