# First-Class Functions: "A Programming language is said to have first-class functions if it treats functions as first-class citizens."

# First-Class Citizen (Programming):
''' A first-class citizen (sometimes called first-class objects) in a programming language is an entity which supports all the
operations generally available to other entities. These operations typically include being passed as an argument, returned from a function, and assigned to a variable. '''

def square(x):
    return x*x

'''
# f= square(5)
f = square #here f is acting as first class funciton

print(f(5))
 '''

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(square, [1,2,3,4,5])
print(squares)

def logger(msg):
    def log_message():
        print('Log', msg)
    return log_message

log_hi = logger('Hello dev')
log_hi()


def html_tag(tag):
    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))
    return wrap_text

print_h1 = html_tag('br') #Means, Run html_tag with 'br', and give the wrap_text function.

print_h1('Test headline !') #first html_tag('br') is run and this func is over and when it said return wrap_text now it will 
print_h1('Another Headline') #perform or take argument for second function which was returned by main function 

# __1__ html_tag('br') → runs html_tag  __2__  tag → becomes "br"  __3__  html_tag → gives back wrap_text
# print_h1 = html_tag('br') → print_h1 = wrap_text → print_h1('Hello') → wrap_text('Hello')

