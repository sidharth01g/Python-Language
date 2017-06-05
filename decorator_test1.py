def foo(x):
    return x


def decorate(my_funct):

    def altered_function(x):
        return my_funct(x) ** 2

    return altered_function


print foo(5)
foo = decorate(foo)
print foo(25)
