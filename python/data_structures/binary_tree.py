class BinaryTree:
    """
    Put docstring here
    """

    def __init__(self):
        self.root = None

    def pre_order(self):
        result = []
        self.pre_order_recursive(self.root, result)
        return result
    
    def in_order(self):
        result = []
        self.in_order_recursive(self.root, result)
        return result
    
    def post_order(self):
        result = []
        self.post_order_recursive(self.root, result)
        return result
    
    def pre_order_recursive(self, node, result):
        if node:
            result.append(node.value)
            self.pre_order_recursive(node.left, result)
            self.pre_order_recursive(node.right, result)

    def in_order_recursive(self, node, result):
        if node:
            self.in_order_recursive(node.left, result)
            result.append(node.value)
            self.in_order_recursive(node.right, result)

    def post_order_recursive(self, node, result):
        if node:
            self.post_order_recursive(node.left, result)
            self.post_order_recursive(node.right, result)
            result.append(node.value)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
