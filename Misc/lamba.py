def get_incementor(delta):
    incrementor_function = lambda x: x + delta
    return incrementor_function

inc_10 = get_incementor(10)
print inc_10(200)
