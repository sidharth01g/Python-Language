import math


def get_nth_root(x, n):
    return x ** (1 / float(n))


def get_nth_power(x, n):
    return x ** n


def get_distance_function(n, f1_pow, f2_root):
    def distance(vector_list):
        sum = 0
        for coordinate in vector_list:
            sum += f1_pow(coordinate, n)
        dist = f2_root(sum, n)
        return dist
    return distance


space_dimension = 3
distance_function = get_distance_function(space_dimension, get_nth_power,
                                          get_nth_root)
distance = distance_function([1, 2, 3])
print distance
