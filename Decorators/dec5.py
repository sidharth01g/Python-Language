import math


def get_square(x):
    return x * x


def get_cube(x):
    return x * x * x


def get_sum_function(f1, f2):
    def sum_function(a):
        return f1(a) + f2(a)
    return sum_function


a = 10
new_function = get_sum_function(get_square, get_cube)
print new_function(a)
new_function1 = get_sum_function(math.sqrt, math.log10)
print new_function1(100)
