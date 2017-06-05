# @wrapt.decorator
def print_neatly(print_something_function):
    def inner(number):
        print("Result: ", end='')
        print_something_function(number)

    # Retain the name of the function that is being decorated
    inner.__name__ = print_something_function.__name__
    return inner

def print_square(number):
    print(number * number)

@print_neatly
def print_cube(number):
    print(number * number * number)

plain = print_square
sugar = print_neatly(plain)

plain(10)
sugar(10)
print_cube(3)

print("Name of print_square function: " + print_square.__name__)
print("Name of print_cube function: " + print_cube.__name__)


"""
Note: Function name has been corrected inside the decorator but there are other
things left undone to create a decorator that work perfectly
http://blog.dscpl.com.au/2014/01/how-you-implemented-your-python.html
Instead use a docorator (import wrapt) written by Graham Dumpleton over the decorator you
create!
"""
