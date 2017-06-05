from node_classes import Node


class BinarySearchTree(object):

    def __init__(self, root):
        self.root = root

    def traverse_inorder(self, current=-1):
        if current == -1:
            current = self.root

        if not current:
            return

        # print(current, current.left_child, current.right_child)

        self.traverse_inorder(current.left_child)
        print(current.data, end =" ")
        self.traverse_inorder(current.right_child)

    def insert(self, data, current=-1):
        if current == -1:
            current = self.root

        if not current:
            try:
                self.root = Node(data)
            except Exception as error:
                print("ERROR: %s" % str(error))
                return False
            return True

        if data < current.data:
            if not current.left_child:
                try:
                    current.left_child = Node(data)
                except Exception as error:
                    print("ERROR: %s" % str(error))
                    return False
                return True
            else:
                self.insert(data, current.left_child)
        elif data > current.data:
            if not current.right_child:
                try:
                    current.right_child = Node(data)
                except Exception as error:
                    print("ERROR: %s" % str(error))
                    return False
            else:
                self.insert(data, current.right_child)
        else:
            return False


def main():
    my_bst = BinarySearchTree(None)

    for data in [1, 9 ,5, 6, 7, 2, 3, 4, 8]:
        my_bst.insert(data)
    my_bst.traverse_inorder()
    print("")


if __name__ == "__main__":
    main()
