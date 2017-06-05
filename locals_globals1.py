a = "Test string"


def test():

    a = "New string"
    print a


test()
print a


def test1(a, b, c):
    print locals()

test1(1, 2, 3)
