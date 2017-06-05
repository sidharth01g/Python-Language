def get_functions():
    def add(a, b):
        return a + b
    def sub(a, b):
        return a - b
    return (add, sub)

sum_function, diff_function = get_functions()
print sum_function(12, 20)
print diff_function(20, 30)


def outer():
    text = "This is sample text"
    def inner():
        return text
    return inner


in1 = outer()
print in1()


def outer1(text):
    def inner1():
        return text
    return inner1


in2 = outer1("Richard")
in3 = outer1("Sara")

print in2()
print in3()
