class StringifyReturn(object):
    def __init__(self, input_function):
        self.input_function = input_function

    def __call__(self, *args, **kwargs):
        return_value = self.input_function(args)
        return str(return_value)

@StringifyReturn
def f1(args):
    return args

print(f1(1, 2, 3))
print(type(f1(1, 2, 3)))
