from node_classes import Node_AVL


class AVLTree(object):

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

    def update_height(self, node):
        if not node:
            return False

        if node.left_child:
            left_height = node.left_child.height
        else:
            left_height = 0

        if node.right_child:
            right_height = node.right_child.height
        else:
            right_height = 0

        node.height = max(left_height, right_height) + 1
        return True

    def update_height_ancestry(self, node):
        current_node = node
        height_before_update = current_node.height
        while current_node:
            self.update_height(current_node)
            if current_node.height == height_before_update:
                break
            current_node = current_node.parent
            if not current_node:
                break
            height_before_update = current_node.height

    def insert(self, data, current=-1):
        if current == -1:
            current = self.root

        if not current:
            try:
                self.root = Node_AVL(data, parent=None)
                self.update_height_ancestry(self.root)
                self.rebalance(self.root)
            except Exception as error:
                print("ERROR: %s" % str(error))
                return False
            return True

        if data < current.data:
            if not current.left_child:
                try:
                    current.left_child = Node_AVL(data, current)
                    self.update_height_ancestry(current.left_child)
                    self.rebalance(current.left_child)
                except Exception as error:
                    print("ERROR: %s" % str(error))
                    return False
                return True
            else:
                self.insert(data, current.left_child)
        elif data > current.data:
            if not current.right_child:
                try:
                    current.right_child = Node_AVL(data, current)
                    self.update_height_ancestry(current.right_child)
                    self.rebalance(current.right_child)
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
        print(current.data, "h:", current.height, end ="    ")
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
            self.update_height_ancestry(parent_node)
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
            self.update_height_ancestry(parent_node)
            target_node = None
            return True

        if target_node.right_child and not target_node.left_child:
            child_subtree_root = target_node.right_child
            child_subtree_root.parent = parent_node
            if target_node is parent_node.left_child:
                parent_node.left_child = child_subtree_root
            else:
                parent_node.right_child = child_subtree_root
            self.update_height_ancestry(parent_node)
            target_node = None
            return True

        # Case 3: Has left as well as right subtrees
        if target_node.right_child and target_node.left_child:
            next_larger_node = self.next_larger(target_node)
            target_node.data = next_larger_node.data
            return self.delete(next_larger_node)

    def height(self, node):
        if node:
            return node.height
        else:
            return 0

    def left_rotate(self, node):
        if not node:
            return
        print("Left rotate at '%s'" % str(node.data))
        right_child = node.right_child
        right_child.parent = node.parent
        if not node.parent:
            self.root = right_child
        else:
            if node is node.parent.left_child:
                node.parent.left_child = right_child
            elif node is node.parent.right_child:
                node.parent.right_child = right_child

        node.right_child = right_child.left_child
        if node.right_child:
            node.right_child.parent = node

        right_child.left_child = node
        node.parent = right_child

        self.update_height_ancestry(node)

    def right_rotate(self, node):
        if not node:
            return
        print("Right rotate at '%s'" % str(node.data))
        left_child = node.left_child
        left_child.parent = node.parent

        if not node.parent:
            self.root = left_child
        else:
            if node is node.parent.left_child:
                node.parent.left_child = left_child
            elif node is node.parent.right_child:
                node.parent.right_child = left_child

        node.left_child = left_child.right_child

        if node.left_child:
            node.left_child.parent = node

        left_child.right_child = node
        node.parent = left_child

        self.update_height_ancestry(node)

    def rebalance(self, node):
        print("\nRebalancing at '%s'" % str(node.data))
        while node:
            self.update_height(node)
            if (self.height(node.left_child) >=
                self.height(node.right_child) + 2):
                if (self.height(node.left_child.left_child) >
                    self.height(node.left_child.right_child)):
                    self.right_rotate(node)
                else:
                    self.left_rotate(node.left_child)
                    self.right_rotate(node)
            if (self.height(node.right_child) >=
                self.height(node.left_child) + 2):
                if (self.height(node.right_child.right_child) >
                    self.height(node.right_child.left_child)):
                    self.left_rotate(node)
                else:
                    self.right_rotate(node.right_child)
                    self.left_rotate(node)
            node = node.parent


def main():
    my_avl = AVLTree(None)

    """
    for data in [1, 9, 6, 7, 2, 3, 4, 8]:
        my_avl.insert(data)
    """
    """
    print("\nIn-order:")
    my_avl.traverse_inorder()
    print("")
    """
    for data in [10, 4, 5, 6, 7]:
        my_avl.insert(data)
        my_avl.traverse_inorder()
        print("")


    print("\nRep invariant: %s" % str(my_avl.check_ri()))
    print("")

    for data in [1, 9 ,5, 6, 7, 2, 3, 4, 8, 0, 5]:
        print("Find %s: %s" % (str(data), my_avl.find(data)))

    print("\nMinimum value: " + str((my_avl.find_min()).data))
    print("\nMaximum value: " + str((my_avl.find_max()).data))

    print("")
    for data in [7, 10, 6]:
        node = my_avl.find(data)
        if not node:
            print("Not found: " + str(data))
            continue
        next_larger_node = my_avl.next_larger(node)
        if not next_larger_node:
            print("No next larger for: " + str(data))
            continue
        print("Next larger of %s: %s" %
              (str(data), str((next_larger_node).data)))


    for data in [7, 10, 6]:
        node = my_avl.find(data)
        if not node:
            print("Not found: " + str(data))
            continue
        next_smaller_node = my_avl.next_smaller(node)
        if not next_larger_node:
            print("No next smaller for: " + str(data))
            continue
        print("Next smaller of %s: %s" %
              (str(data), str((next_smaller_node).data)))

    print("=" * 100)
    my_avl_2 = AVLTree(None)
    for data in [5, 4, 10, 8, 7, 20, 15, 30]:
        my_avl_2.insert(data)
    my_avl_2.traverse_inorder()
    print("")
    print(my_avl_2.delete(my_avl_2.find(5)))
    my_avl_2.traverse_inorder()
    print("")
    print(my_avl_2.delete(my_avl_2.find(4)))
    my_avl_2.traverse_inorder()
    print("")
    print(my_avl_2.delete(my_avl_2.find(8)))
    my_avl_2.traverse_inorder()
    print("")
    print(my_avl_2.delete(my_avl_2.find(20)))
    my_avl_2.traverse_inorder()
    print("")


if __name__ == "__main__":
    main()
