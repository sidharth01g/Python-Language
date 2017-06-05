def outer():
    x = 20
    def inner():
        print x
        print locals()
    inner()

print dir(outer)
print outer.__class__
print outer.__sizeof__()
print dir(outer.__code__)
outer()
