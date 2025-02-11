# TODO: Create the logging_decorator() function ?
def logging_decorator(function):
    def wrapped_function(*args):
        print(f"You called {function.__name__}{args}")
        result = function(*args)
        print(f"It returned: {result}")
        return result # needs to return because result is local variable. not global variable
    return wrapped_function


# TODO: Use the decorator ?
@logging_decorator
def a_function(*args):
    return sum(args)


a_function(1, 2, 3)