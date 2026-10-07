# def square_numbers(nums):
#     result = []
#     for i in nums:
#         result.append(i*i)
#     return result

# my_nums = square_numbers([1,2,3,4,5])

# print(my_nums)


#--------------------------------------------------

# def square_numbers(nums):
#     for i in nums:
#         yield (i*i)

# my_nums = square_numbers([1,2,3,4,5])
# print(my_nums) #gives it's generator
# print(next(my_nums)) #gives 1 as 
# print(next(my_nums)) #gives 4 as 
# print(next(my_nums)) #gives 9 as 
# print(next(my_nums)) #gives 16 as 
# print(next(my_nums)) #gives 25 as 
# # print(next(my_nums)) #gives error

# for i in my_nums:
#     print(i)

#------------------using list comprehension -------------------------
my_nums = [x*x for x in [1,2,3,4,5]]
print(my_nums)

for i in my_nums:
    print(i)

#if used () instead [] in comprehension we get generator

my_nums = (x*x for x in [1,2,3,4,5])
print(my_nums) # generator object
print(list(my_nums)) # convert them into list

'''
generator is much faster than usual function when parameter is large
import mem_profile
import random
import time

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

print 'Memory (Before): {}Mb'.format(mem_profile.memory_usage_psutil())

def people_list(num_people):
    result = []
    for i in xrange(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        result.append(person)
    return result

def people_generator(num_people):
    for i in xrange(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        yield person

# t1 = time.clock()
# people = people_list(1000000) #normal list
# t2 = time.clock()

t1 = time.clock()
people = people_generator(1000000)  #generator
t2 = time.clock()

t1 = time.clock()
people = list(people_generator(1000000))  #if we convert generator into list it will give time equivalent to list only
t2 = time.clock()

print 'Memory (After) : {}Mb'.format(mem_profile.memory_usage_psutil())
print 'Took {} Seconds'.format(t2-t1)
'''