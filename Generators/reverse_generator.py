def reverse(data_string):
    for i in range(len(data_string) -1, -1, -1):
        yield data_string[i]


my_name = "Sidharth Gopakumar"
rev = reverse(my_name)
print rev
print list(rev)
print list(rev)
for char in rev:
    print char,
