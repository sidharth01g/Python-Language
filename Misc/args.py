def show_args(*args):
    for arg in args:
        print(arg)

args_list = [1, 2 ,3 ,4, "What!", {1:2, 3:4}, [1, "sdaf"]]
show_args(args_list)
print('*' * 50)
show_args(*args_list)
