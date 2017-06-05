def test():
    return  'ABC'


# print test()

a_string = 'Hello World'
print globals()


def show_vars():
    my_var = "asdfasdf"
    def f1():
        x = 10
        print x
    print globals()
    print locals()


print show_vars()
