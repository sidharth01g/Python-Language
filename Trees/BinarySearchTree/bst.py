import math

# from node_classes import Node


class BinarySearchTree(object):

    def __init__(self, size, min_interval):
        self.array_list = [None for i in range(size)]
        self.min_interval = min_interval

    def parent_index(self, index):
        return int((index - 1) / 2)

    def left_child_index(self, index):
        return index * 2 + 1

    def right_child_index(self, index):
        return index * 2 + 2

    def insert(self, data, root_index=0):
        if root_index >= len(self.array_list):
            print("ERROR: Array is full!")
            return -1
        if self.array_list[root_index] is None:
            self.array_list[root_index] = data
            return root_index
        else:
            diff = data - self.array_list[root_index]
            if math.fabs(diff) < self.min_interval:
                print("ERROR: No good slot available")
                return -1
            else:
                if diff > 0:
                    return self.insert(data, self.right_child_index(root_index))
                else:
                    return self.insert(data, self.left_child_index(root_index))


def main():
    my_bst = BinarySearchTree(10, 3)
    print(my_bst.array_list)
    print("-->", my_bst.insert(25))
    print(my_bst.array_list)
    print("-->", my_bst.insert(29))
    print(my_bst.array_list)


if __name__ == "__main__":
    main()
