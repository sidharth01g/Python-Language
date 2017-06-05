def stringify_return(input_function):
    def wrapper_function():
        return_value = input_function()
        # print("Convert return value to string")
        return str(return_value)
    return wrapper_function

def f1():
    return [1, 2, 3]

@stringify_return
def f1_decorated():
    return [1, 2, 3]

print(type(f1()))
print(type(f1_decorated()))
