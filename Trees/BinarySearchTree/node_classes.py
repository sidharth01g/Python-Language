class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.left_child = None
        self.right_child = None

class Node_X(Node):
    def __init__(self, data, parent=None):
        Node.__init__(self, data)
        self.parent = parent

    def next_larger(self):
        if not self:
            return None

class Node_AVL(Node_X):
    def __init__(self, data, parent=None, height=None):
        Node_X.__init__(self, data, parent)
        self.height = height
