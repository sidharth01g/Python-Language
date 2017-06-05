def outer():
    hi = "Hi! "
    def inner(message):
        print hi + message
    return inner

f = outer()
f("What the hell!")
