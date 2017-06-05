from node_classes import Node_X


class BinarySearchTree_X(object):

    def __init__(self, root):
        self.root = root

    def check_ri(self, current=-1):

        """
        Checks representation invariance.
        Prints error_message if it is violated
        """
        if current == -1:
            current = self.root

        if not current:
            return True

        # Initialize to True
        representation_invariant = True

        # Check left subtree
        representation_invariant = (
            self.check_ri(current.left_child) or
            representation_invariant)

        # Check current node
        print(current.data, end =" ")
        if current.left_child:
            if current.data <= current.left_child.data:
                error_message = (
                    "Representation invariance failed at left child of %s" %
                    str(current.data))
                # raise Exception(error_message)
                print(error_message)
                representation_invariant = False
        if current.right_child:
            if current.data >= current.right_child.data:
                error_message = (
                    "Representation invariance failed at right child of %s" %
                    str(current.data))
                # raise Exception(error_message)
                print(error_message)
                representation_invariant = False

        # Check right subtree
        representation_invariant = (
            self.check_ri(current.right_child) or
            representation_invariant)

        return representation_invariant

    def insert(self, data, current=-1):
        if current == -1:
            current = self.root

        if not current:
            try:
                self.root = Node_X(data, parent=None)
            except Exception as error:
                print("ERROR: %s" % str(error))
                return False
            return True

        if data < current.data:
            if not current.left_child:
                try:
                    current.left_child = Node_X(data, current)
                except Exception as error:
                    print("ERROR: %s" % str(error))
                    return False
                return True
            else:
                self.insert(data, current.left_child)
        elif data > current.data:
            if not current.right_child:
                try:
                    current.right_child = Node_X(data, current)
                except Exception as error:
                    print("ERROR: %s" % str(error))
                    return False
            else:
                self.insert(data, current.right_child)
        else:
            return False

    def traverse_inorder(self, current=-1):
        if current == -1:
            current = self.root

        if not current:
            return

        self.traverse_inorder(current.left_child)
        print(current.data, end =" ")
        self.traverse_inorder(current.right_child)

    def find(self, value, current=-1):
        if current == -1:
            current = self.root

        # Base case 1
        if not current:
            return None

        # Base case 2
        if current.data == value:
            print("Found " + str(value))
            return current

        if value > current.data:
            return self.find(value, current.right_child)
        if value < current.data:
            return self.find(value, current.left_child)

    def find_min(self, current=-1):
        if current == -1:
            current = self.root

        if not current:
            return None

        if not current.left_child:
            return current

        return self.find_min(current.left_child)

    def find_max(self, current=-1):
        if current == -1:
            current = self.root

        if not current:
            return None

        if not current.right_child:
            return current

        return self.find_max(current.right_child)

    def next_larger(self, current=-1):
        if current == -1:
            current = self.root

        if not current:
            return None

        if current.right_child:
            # Has a right subtree
            return self.find_min(current.right_child)
        else:
            # Does not have a right subtree
            temp = current
            while True:
                if not temp.parent:
                    # temp has reached root with no right subtree there
                    # - current is the largest
                    return None

                if temp is temp.parent.right_child:
                    temp = temp.parent
                else:
                    return temp.parent

    def next_smaller(self, current=-1):
        if current == -1:
            current = self.root

        if not current:
            return None

        if current.left_child:
            # Has a left subtree
            return self.find_max(current.left_child)
        else:
            # Does not have a left subtree
            temp = current
            while True:
                if not temp.parent:
                    # temp has reached root & there is no left subtree for root
                    # - current is the smallest node
                    return None

                if temp is temp.parent.left_child:
                    temp = temp.parent
                else:
                    return temp.parent

    def delete(self, target_node):
        if not target_node:
            return False

        parent_node = target_node.parent

        # Case 1: No children
        if (not target_node.left_child) and (not target_node.right_child):
            if target_node is parent_node.left_child:
                parent_node.left_child = None
            if target_node is parent_node.right_child:
                parent_node.right_child = None
            target_node = None
            return True

        # Case 2: Has one subtree
        if target_node.left_child and not target_node.right_child:
            child_subtree_root = target_node.left_child
            child_subtree_root.parent = parent_node
            if target_node is parent_node.left_child:
                parent_node.left_child = child_subtree_root
            else:
                parent_node.right_child = child_subtree_root
            target_node = None
            return True

        if target_node.right_child and not target_node.left_child:
            child_subtree_root = target_node.right_child
            child_subtree_root.parent = parent_node
            if target_node is parent_node.left_child:
                parent_node.left_child = child_subtree_root
            else:
                parent_node.right_child = child_subtree_root
            target_node = None
            return True

        # Case 3: Has left as well as right subtrees
        if target_node.right_child and target_node.left_child:
            next_larger_node = self.next_larger(target_node)
            target_node.data = next_larger_node.data
            return self.delete(next_larger_node)


def main():
    my_bst = BinarySearchTree_X(None)

    """
    for data in [1, 9, 6, 7, 2, 3, 4, 8]:
        my_bst.insert(data)
    """
    """
    print("\nIn-order:")
    my_bst.traverse_inorder()
    print("")
    """
    for data in [10, 4, 5, 6, 7]:
        my_bst.insert(data)

    print("\nRep invariant: %s" % str(my_bst.check_ri()))
    print("")

    for data in [1, 9 ,5, 6, 7, 2, 3, 4, 8, 0, 5]:
        print("Find %s: %s" % (str(data), my_bst.find(data)))

    print("\nMinimum value: " + str((my_bst.find_min()).data))
    print("\nMaximum value: " + str((my_bst.find_max()).data))

    print("")
    for data in [7, 10, 6]:
        node = my_bst.find(data)
        if not node:
            print("Not found: " + str(data))
            continue
        next_larger_node = my_bst.next_larger(node)
        if not next_larger_node:
            print("No next larger for: " + str(data))
            continue
        print("Next larger of %s: %s" %
              (str(data), str((next_larger_node).data)))


    for data in [7, 10, 6]:
        node = my_bst.find(data)
        if not node:
            print("Not found: " + str(data))
            continue
        next_smaller_node = my_bst.next_smaller(node)
        if not next_larger_node:
            print("No next smaller for: " + str(data))
            continue
        print("Next smaller of %s: %s" %
              (str(data), str((next_smaller_node).data)))

    print("=" * 100)
    my_bst_2 = BinarySearchTree_X(None)
    for data in [5, 4, 10, 8, 7, 20, 15, 30]:
        my_bst_2.insert(data)
    my_bst_2.traverse_inorder()
    print("")
    print(my_bst_2.delete(my_bst_2.find(5)))
    my_bst_2.traverse_inorder()
    print("")
    print(my_bst_2.delete(my_bst_2.find(4)))
    my_bst_2.traverse_inorder()
    print("")
    print(my_bst_2.delete(my_bst_2.find(8)))
    my_bst_2.traverse_inorder()
    print("")
    print(my_bst_2.delete(my_bst_2.find(20)))
    my_bst_2.traverse_inorder()
    print("")


if __name__ == "__main__":
    main()
