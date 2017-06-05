a = [i for i in range(10)]

def square(a_list):
    for number in a_list:
        yield number * number

square_generator = square(a)
print square_generator
print list(square_generator)
