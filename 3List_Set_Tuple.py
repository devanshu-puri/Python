print("\n=== LISTS ===")
courses = ['history', 'math', 'physics', 'compsci']

# len() counts items; indexing starts at 0 and negative indexes start at the end.
print(len(courses))
print(courses[0])
print(courses[-1])

# Slicing returns a portion: [start:stop:step], where stop is not included.
print(courses[1:3]) #index 3 is not included
print(courses[::-1]) #reverse 

# Lists are ordered and MUTABLE, so items can be changed.
courses[1] = 'calculus'
courses.append('biology')  # add one item at the end
courses.insert(1, 'english')  # add an item at a position
courses.extend(['art', 'music'])  # add multiple items
print(courses)

# Remove items with remove(), pop(), or del.
courses.remove('art')  # remove by value; raises ValueError if missing
last_course = courses.pop()  # pop return the value that was removed , so to store we used last_course
del courses[1]  # delete by index or slice
print(last_course, courses)


# Useful list operations and methods.
print()
print("# Useful list operations and methods. ")
print('calculus' in courses)  # membership test
print(courses.index('calculus'))  # find an item's index
print(courses.count('calculus'))  # count occurrences
courses.sort()  # sort the list in place
print(courses)
reversed_courses = sorted(courses, reverse=True)  # returns a new sorted list
print(reversed_courses)

# copy() prevents changes to the copy from changing the original list.
courses_copy = courses.copy()
courses_copy.clear()  # remove every item from the copy
print(courses, courses_copy)

# List comprehension creates a list from an expression and optional condition.
short_courses = [course for course in courses if len(course) < 6]  #"Give me course, for every course in courses, if its length is less than 5."
print(short_courses)

print("\n=== SETS ===")
# A set is unordered, contains unique values, and is mutable.
skills = {'python', 'sql', 'python', 'git'}
skills.add('linux')
print(skills)
skills.update(['docker', 'git'])
print(skills)
skills.discard('unknown')  # safe if the item is absent
skills.remove('git')  # raises KeyError if the item is absent
print(skills)

# Set operations compare groups of values.
backend = {'python', 'sql', 'git'}
devops = {'git', 'docker', 'linux'}
print(backend | devops)  # union: items in either set
print(backend & devops)  # intersection: items in both sets
print(backend - devops)  # difference: items only in backend
print(backend ^ devops)  # symmetric difference: items in exactly one set
print(backend.issubset(backend | devops))

#loop
Subject = ['Math', 'History', 'Physics', 'compSci']
for index, course in enumerate(Subject):
    print(index, course)

# if dont want index to start from 0 , instead 1
for index, course in enumerate(Subject, start=1):
    print(index, course)

course_str = ', '.join(Subject)
new_list = course_str.split(' - ')
print(course_str) 
print(new_list)

print("\n=== TUPLES ===")
# A tuple is ordered like a list but immutable after creation, can't modify
person = ('Ava', 25, 'developer')
print(person[0], person[1:])
print(person.count('developer'))
print(person.index(25))

# Tuple unpacking assigns tuple items to variables.
name, age, job = person
print(name, age, job)
name, *details = person  # starred unpacking collects the remaining items
print(name, details)

# Use a one-item comma to create a tuple; parentheses alone are not enough.
one_item_tuple = ('python',)
print(type(one_item_tuple))

# Convert between common collection types when needed.
print(tuple(courses))
print(list(skills))
print(set(['python', 'python', 'sql']))  # removes duplicates

#set also have , x.intersection(y), x.union(y), x.difference(y)

#Empty list 
empty_list = []
empty_list = list()

#Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

#Empty Set
empty_set = {} #this isn't right! It's a dictionary
empty_set = set()