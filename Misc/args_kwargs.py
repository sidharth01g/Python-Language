def show_all(*args, **kwargs):

    print("Args:")
    for arg in args:
        print(arg)

    print("Keyword arguments:")
    for item in kwargs.items():
        print item


show_all(1, 2, "Wow", x = [10, 20, 30], y = "www")
