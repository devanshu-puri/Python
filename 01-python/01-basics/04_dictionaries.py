print("\n=== DICTIONARIES ===")

# A dictionary stores data as key-value pairs.
student = {
	'name': 'John',
	'age': 35,
	'courses': ['Math', 'CompSci']
}
print(student)

# Access values with their keys.
print(student['name'])
print(student.get('email'))  # None when the key is missing
print(student.get('email', 'No email provided'))

# Add new values and update existing values.
student['email'] = 'john@example.com'
student['age'] = 36
#useful when updating multiple value at time, take dict as argument
student.update({'city': 'London', 'active': True})
print(student)

# Check keys and count key-value pairs.
print('name' in student)
print('email' in student)
print(len(student))

# Remove values.
removed_city = student.pop('city')
print(removed_city)
student.pop('unknown', None)  # safe if the key is missing
print(student)

# Inspect keys, values, or both.
print(student.keys())
print(student.values())
print(student.items()) #key and value

# Iterate over dictionaries.
for key, value in student.items():
	print(key, '=', value)

# Lists of dictionaries are common for API responses and database results.
users = [
	{'name': 'Ava', 'role': 'admin'},
	{'name': 'Sam', 'role': 'user'}
]

for user in users:
	print(user['name'], user['role'])

# Nested dictionaries store related data.
users_by_id = {
	1: {'name': 'Ava', 'role': 'admin'},
	2: {'name': 'Sam', 'role': 'user'}
}
print(users_by_id[1]['name'])
users_by_id[2]['role'] = 'editor'
print(users_by_id)

# Dictionary comprehensions create dictionaries from an iterable.
numbers = [1, 2, 3, 4, 5]
squares = {number: number ** 2 for number in numbers}
even_squares = {
	number: number ** 2
	for number in numbers
	if number % 2 == 0
}
print(squares)
print(even_squares)

# zip() combines related sequences into a dictionary.
names = ['Ava', 'Sam', 'Mia']
ages = [25, 30, 22]
people = dict(zip(names, ages))
print(people)

# Count items with get().
words = ['python', 'sql', 'python', 'git', 'sql', 'python']
word_counts = {}

for word in words:
	word_counts[word] = word_counts.get(word, 0) + 1

print(word_counts)

# Group values with setdefault().
employees = [
	('Ava', 'backend'),
	('Sam', 'ai'),
	('Mia', 'backend')
]
employees_by_department = {}

for name, department in employees:
	employees_by_department.setdefault(department, []).append(name)

print(employees_by_department)

# Assignment creates an alias; copy() creates a shallow copy.
original = {'name': 'Ava'}
copied = original.copy()
copied['name'] = 'Sam'
print(original)
print(copied)

# Merge dictionaries. Later values replace earlier values for duplicate keys.
settings = {'host': 'localhost', 'port': 8000}
extra_settings = {'port': 9000, 'debug': True}
combined_settings = {**settings, **extra_settings}
print(combined_settings)