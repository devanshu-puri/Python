import my_module as mm
#or to cut down more = from my_module import find_index, give access to only one function
# index = find_index(courses, 'Math')

courses = ['History', 'Math', 'Physics', 'CompSci']

index = mm.find_index(courses, 'Math')
print(index)