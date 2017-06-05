def sum(a, b):
    return a + b


def diff(a, b):
    return a - b


def my_function(function_1, function_2, a, b):
    return function_1(a, b) * function_2(a, b)

x = 5
y = 4
z = my_function(sum, diff, x, y)
print z
