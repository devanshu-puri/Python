""" 
# 2. The Challenge
users = ['ava', 'sam', 'mia']
roles = ['admin', 'editor', 'viewer']
# Build user_to_role, then find all users who can edit content.


user_to_role = {
  'ava' : ['admin', 'editor'],
  'sam' : ['editor', 'viewer'],
  'mia' : ['viewer']
}


editor = [
  user
  for user, user_role in user_to_role.items()
  if "editor" in user_role
]

print(editor) 

"""

#-----------------------------------------------------------------------------------------#  

'''
# 3. My Current Python Toolkit
# zip pairs related values; dict stores fast key -> value lookups; a loop filters results.

users = ["ava", "sam", "mia", "leo"]
scores = [85, 62, 91, 74]

""" Your tasks:
1. Use zip() to pair each user with their score.
2. Build a dictionary called user_scores.
3. Find all users who scored at least 80.
4. Store their names in a list called qualified_users. """

""" instead
user_scores = {
    "ava" : 85,
    "sam" :62, 
    "mia" : 74, 
    "leo" : 91
} """

user_scores =dict(zip(users, scores))

ans = {
    user:user_val
    for user,user_val in user_scores.items() if user_val >= 80 
}

print(user_scores)
print(ans)

'''

#-----------------------------------------------------------------------------------------#  


""" prints only ['ava', 'sam']
#zip stops as soon as iterator run out of element

#if still want to take mia with null 

from itertools import zip_longest

users = ['ava', 'sam', 'mia']
roles = ['admin', 'editor']

user_to_role = dict(
    zip_longest(users, roles, fillvalue=None)
)

print(user_to_role)

"""


#-----------------------------------------------------------------------------------------#  

# 5 same concpets

#-----------------------------------------------------------------------------------------#  


# Q1. What happens when roles has fewer items than users?
#     Use the example in Section 4 to determine the result.
#
# Q2. What happens when two users have the same role?
#     Use the example in Section 4 to explain the behavior.
#
# Q3. Why is a dictionary better than repeatedly scanning two lists?
#     Compare looking up a user's role in a dictionary with
#     finding the user's index in a list and accessing the role
#     at the same index.
#
# Q4. How would you represent a user with multiple roles?
#     Assume Ava can be both an admin and a viewer.
#     Write the dictionary entry that represents this.
#
# Q5. Does this mapping alone separate Tenant A from Tenant B?
#     Assume both tenants can have a user named 'sam'.
#     Explain why a username-only mapping cannot distinguish them.

#1
""" users = ['ava', 'sam', 'mia']
roles = ['admin', 'editor']

mapping = dict(zip(users, roles))
print(mapping) """
#output = {'ava': 'admin', 'sam': 'editor'}

#2
""" users = ['ava', 'sam']
roles = ['editor', 'editor']

mapping = dict(zip(users, roles)) """

#output 2 = {'ava': 'editor', 'sam': 'editor'}

#3
""" users = ['ava', 'ava']
roles = ['admin', 'viewer']

print(dict(zip(users, roles))) """
#output ={'ava': 'viewer'}, However, if the same username appears twice with different roles,
# the later value overwrites the earlier one
