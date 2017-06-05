def repeat_thrice(message):
    return message * 3

def print_result(any_function):
    def new_function(message):
        print any_function(message)
    return new_function


new_function = print_result(repeat_thrice)
new_function(" \m/ ")
