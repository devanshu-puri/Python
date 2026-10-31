message = 'Hello World'
print('Hello World')
print()
print(message)

#quoatation issue
new = 'Bobby\'s World'
new_2 = "Bobby's World"

#multi line 
multi = '''
Bobby's World was  a good
cartoon in 1990s.

'''
print(multi)

#lenght of string
print(len(message))

#first character
print(message[0])

#last character
print(message[10])

#extract only Hello
print(message[0:5]) 
#or print(message[:5])

#print last word
print(message[6:])

#to lower-case
print(message.lower())

#to upper-case
print(message.upper())

print(message.count('hello'))

print(message.find('World'))

new_message = message.replace('World', '_Universe')

print(new_message)

#formated string


greeting = "hello"
name = "MICHAEl"
message = '{}, {}. Welcome !'.format(greeting,  name)
print(message)

message = f'{greeting}, {name}.Welcome!'
print(message)

#dir method show all the attribute and method used for that variable
print(dir(name))

#to know more detail, write it's datatype
print(help(str))