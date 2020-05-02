from functools import wraps
# This decorator copies the lost metadata from the undecorated function to the decorated closure.


def split_string(func):
    def wrapper():
        text = func()
        return text.split()

    return wrapper


def uppercase_decorator(func):
    @wraps(func)
    def wrapper():
        text = func()
        return text.upper()

    return wrapper


# We notice that the application of decorators is from the bottom up.
# The sentence has first been converted to uppercase and then split into a list.
@split_string
@uppercase_decorator
def say_hi():
    """Docstring"""
    return 'hello there'


print(say_hi())

# say_hi.__name__
# say_hi.__doc__



# def uppercase_decorator(function):
#     def wrapper():
#         func = function()
#         make_uppercase = func.upper()
#         return make_uppercase
#     return wrapper
