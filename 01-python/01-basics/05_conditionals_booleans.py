print("\n=== CONDITIONALS AND BOOLEAN VALUES ===")

# Comparisons produce True or False.
age = 25
print(age == 25)
print(age != 30)
print(age > 18)
print(age <= 20)

# if, elif, and else choose which block runs.
score = 82

if score >= 90:
	grade = 'A'
elif score >= 80:
	grade = 'B'
elif score >= 70:
	grade = 'C'
else:
	grade = 'Needs improvement'

print(grade)

# and requires every condition to be true.
has_id = True

if age >= 18 and has_id:
	print('Entry allowed')
else:
	print('Entry denied')

# or requires at least one condition to be true.
is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
	print('No work today')

# not reverses a Boolean value.
is_logged_in = False

if not is_logged_in:
	print('Please log in')

# Empty values are false-like in conditions.
username = ''
items = []

if not username:
	print('Username is missing')

if not items:
	print('There are no items')

print(bool(1))
print(bool(0))
print(bool('Python'))
print(bool(''))
print(bool([]))

# Membership checks.
allowed_roles = ['admin', 'editor']
print('admin' in allowed_roles)
print('guest' not in allowed_roles)

user = {'name': 'Ava', 'role': 'admin'}
print('name' in user)  # checks dictionary keys
print('Ava' in user.values())  # checks dictionary values

# Chained comparisons are useful for ranges.
temperature = 22

if 18 <= temperature <= 25:
	print('Comfortable temperature')

# Use == for values and is for identity, especially with None.
first = [1, 2]
second = [1, 2]
print(first == second)

result = None
if result is None:
	print('No result')

# Conditional expressions are useful for simple choices.
number = 7
number_type = 'even' if number % 2 == 0 else 'odd'
print(number_type)

# Short-circuiting safely checks optional values.
optional_user = None

if optional_user and optional_user.get('active'):
	print('Active user')
else:
	print('User is missing or inactive')

# and/or can provide fallback values.
name = ''
display_name = name or 'Anonymous'
print(display_name)

# Parentheses make complex conditions easier to understand.
is_admin = False
is_owner = True
is_active = True

if (is_admin or is_owner) and is_active:
	print('Access allowed')

# Guard clauses return early for invalid cases.
def process_order(order):
	if not order:
		return 'Order is missing'

	if order['total'] <= 0:
		return 'Invalid total'

	return 'Order processed'


print(process_order(None))
print(process_order({'total': 0}))
print(process_order({'total': 50}))

# any() checks whether at least one item is true.
# all() checks whether every item is true.
scores = [75, 82, 90]
print(any(score < 50 for score in scores))
print(all(score >= 50 for score in scores))

# Conditions can be used inside comprehensions.
numbers = range(1, 11)
odd_numbers = [number for number in numbers if number % 2 != 0]
print(odd_numbers)

# A safe dictionary lookup avoids KeyError for missing optional keys.
account = {'name': 'Ava'}

if account.get('role') == 'admin':
	print('Admin access')
else:
	print('Regular access')

# Practical order classification example.
order = {
	'paid': True,
	'shipped': False,
	'cancelled': False
}

if order['cancelled']:
	print('Cancelled')
elif order['shipped']:
	print('Shipped')
elif order['paid']:
	print('Ready to ship')
else:
	print('Payment required')
