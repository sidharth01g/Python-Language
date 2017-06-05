def decorate(my_funct):

    def altered_function(x):
        return my_funct(x) ** 2

    return altered_function


@decorate
def foo(x):
    return x


print foo(5)
