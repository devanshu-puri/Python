# ITERABLES AND ITERATORS
# Core idea: an iterable produces an iterator.

# 1) A list is iterable
numbers = [1, 2, 3]
print("List:", numbers)
print("Has __iter__?", hasattr(numbers, "__iter__"))

# 2) iter() gives us an iterator object
it = iter(numbers)
print("Iterator object:", it)
print("Next value:", next(it))
print("Next value:", next(it))
print("Next value:", next(it))

# StopIteration happens when the iterator is exhausted
try:
    print("Next value:", next(it))
except StopIteration:
    print("Iterator is exhausted")

# 3) A for-loop hides this machinery
for num in numbers:
    print("for-loop value:", num)

# 4) Strings are iterable too
for ch in "python":
    print(ch, end=" ")
print()

# 5) Custom iterator
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

print("Custom iterator:")
for x in Countdown(3):
    print(x)

# 6) Generator function
# Generators are a very common Python pattern

def squares(n):
    for i in range(1, n + 1):
        yield i * i

print("Squares:", list(squares(5)))

# 7) Why this matters
# Iterators are used heavily when processing files, DB results, API data,
# streaming inputs, and large data sets without loading everything at once.
