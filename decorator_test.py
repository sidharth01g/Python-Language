import math


def square_of(x):
    return x ** 2


def get_sum_of_square_function(square_function):

    def sum_of_squares(a, b):
        return square_function(a) + square_function(b)

    return sum_of_squares


sigma_square_function = get_sum_of_square_function(square_of)
sum = sigma_square_function(3, 4)
print sum
