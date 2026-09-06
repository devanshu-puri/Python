print("\n=== LOOPS AND ITERATION ===")

# A for loop visits each item in an iterable.
courses = ['Python', 'SQL', 'FastAPI']

for course in courses:
	print(course)

# range() generates a sequence of numbers.
for number in range(1, 4):
	print(number)

for number in range(0, 10, 2):
	print(number)

# enumerate() gives both the index and the item.
for index, course in enumerate(courses, start=1):
	print(index, course)

# zip() loops through related values together.
names = ['Ava', 'Sam', 'Mia']
roles = ['backend', 'ai', 'data']

for name, role in zip(names, roles):
	print(name, role)

# Loop through dictionaries using items().
user = {'name': 'Ava', 'role': 'admin'}

for key, value in user.items():
	print(key, '=', value)

# continue skips the current iteration.
for number in range(1, 6):
	if number == 3:
		continue
	print('continue example:', number)

# break stops the loop immediately.
for number in range(1, 6):
	if number == 4:
		break
	print('break example:', number)

# pass does nothing and can be used as a temporary placeholder.
for number in range(3):
	if number == 1:
		pass
	print('pass example:', number)

# A while loop continues while its condition is true.
count = 1

while count <= 3:
	print('while:', count)
	count += 1

# Use a break condition to stop a while loop safely.
attempts = 0

while True:
	attempts += 1
	print('attempt:', attempts)

	if attempts == 3:
		break

# Nested loops are useful for grids and grouped data.
for row in range(1, 3):
	for column in range(1, 4):
		print('position:', row, column)

# A loop can build a result.
numbers = [1, 2, 3, 4, 5]
squares = []

for number in numbers:
	squares.append(number ** 2)

print(squares)

# The equivalent list comprehension is concise and Pythonic.
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

# Find the first matching item and stop early.
target_user = None

for current_user in [
	{'name': 'Ava', 'active': False},
	{'name': 'Sam', 'active': True},
	{'name': 'Mia', 'active': True}
]:
	if current_user['active']:
		target_user = current_user
		break

print(target_user)

# Avoid changing a collection while directly iterating over it.
values = [1, 2, 3, 4, 5]
odd_values = [value for value in values if value % 2 != 0]
print(odd_values)

# Strings are iterable too.
for character in 'Python':
	print(character)

# Create an iterator with iter() and retrieve values with next().
course_iterator = iter(courses)
print(next(course_iterator))
print(next(course_iterator))

# StopIteration is raised when an iterator has no remaining values.
course_iterator = iter(['one'])
print(next(course_iterator))

try:
	print(next(course_iterator))
except StopIteration:
	print('The iterator is exhausted')

# Practical example: calculate a total.
prices = [12.50, 8.00, 5.50]
total = 0

for price in prices:
	total += price

print('total:', total)

# Practical example: count successful records.
statuses = ['success', 'failed', 'success', 'success']
success_count = 0

for status in statuses:
	if status == 'success':
		success_count += 1

print('successful records:', success_count)
