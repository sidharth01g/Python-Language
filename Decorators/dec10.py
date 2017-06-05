def stringify_return(input_function):
    def wrapper_function(*args, **kwargs):
        return_value = input_function(args)
        # print("Convert return value to string")
        return str(return_value)
    return wrapper_function

@stringify_return
def f1(args):
    return args

print(f1(1, 2, 3))
print(type(f1(1, 2, 3)))
