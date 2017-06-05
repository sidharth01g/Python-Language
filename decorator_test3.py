def show_args(function):
    def new_function(*args):
        print "Arguments: ", args
        return sum_function(args)
    return new_function


@show_args
def sum_function(numbers_list):
    sum = 0
    # for t in numbers_list:
    #     if type(t) is float or type (t) is int:
    #         sum += t
    return sum


print sum_function(12, 13, 14)
