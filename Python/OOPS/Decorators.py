# Decorators

def outer_function(msg):
    message = msg
    def inner_function():
        print(message)
    return inner_function

hi_func = outer_function('Hello')
by_func = outer_function('Tata')
hi_func()
by_func()
