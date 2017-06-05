import math


def get_result_function(old_function):
    def get_result(a, b):
        return old_function(a*a + b*b)
    return get_result


@get_result_function
def inverse(x):
    return 1.0/x




a = 4.0
b = 5.0

my_hypotenuse_function = get_result_function(math.sqrt)
c = my_hypotenuse_function(a, b)

print a ,b, c

print a, b, inverse(a, b)
