def outer_func(msg):
    message = msg

    def inner_func():
        print(message)

    return inner_func

my_func = outer_func()
my_func() 