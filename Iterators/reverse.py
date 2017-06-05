#!/usr/bin/python3
class Reverse:

    def __init__(self, data_string):
        self.data_string = data_string
        self.index = len(data_string)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data_string[self.index]


my_name = "Sidharth Gopakumar"
rev = Reverse(my_name)
for character in rev:
    print(character,)
