# int: a whole number without a decimal point.
whole_number = 10

# float: a number that contains a decimal point.
decimal_number = 3.14
print(type(decimal_number))  # type() tells us the value's data type.

# Basic arithmetic operators work with numeric values.
print(whole_number + 2)  # addition
print(whole_number - 2)  # subtraction
print(whole_number * 2)  # multiplication
print(whole_number / 2)  # division; / returns a float
print(whole_number // 3)  # floor division; returns the whole-number part
print(whole_number % 3)  # modulus; returns the remainder
print(whole_number ** 2)  # exponentiation; raises a number to a power

# Convert compatible text into a numeric value.
number_from_text = int("25")
print(number_from_text)

print(abs(-3)) # absolute value

print(round(3.75)) # round of value
print(round(3.75523, 1)) #how much value to round off

# Numeric literals can use underscores to improve readability.
large_number = 1_000_000

# Floating-point values can have tiny precision errors because computers store
# them in binary; use Decimal when exact decimal arithmetic is important.
print(0.1 + 0.2)
from decimal import Decimal
print(Decimal("0.1") + Decimal("0.2"))

# Complex numbers contain a real part and an imaginary part.
complex_number = 2 + 3j
print(complex_number.real, complex_number.imag)

# Comparisons produce Boolean values: True or False.
print(whole_number > 5)
print(whole_number == 10)

# Bitwise operators work on the binary bits of integers.
print(5 & 3)  # AND
print(5 | 3)  # OR
print(5 << 1)  # shift bits left; commonly doubles the value

# Augmented assignment updates a variable using its current value.
whole_number += 5
print(whole_number)

#Casting string to integer

num_1 = '100'
num_2 = '200' 

print(int(num_1) + int(num_2))