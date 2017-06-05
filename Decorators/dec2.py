
def get_square(x):
    return x*x

def get_inverse(x):
    return 1.0/x

def add_one(orig_function):
    def new_funct(x):
        return orig_function(x) + 1
    return new_funct


print get_square(12)
new_funct1 = add_one(get_square)
print new_funct1(12)

print get_inverse(10)
new_funct2 = add_one(get_inverse)
print new_funct2(10)
