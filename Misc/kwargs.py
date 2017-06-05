def show_kwargs(**kwargs):
    for item in kwargs.items():
        print item


show_kwargs(a=25, b={1:2, 3:"asd"})
