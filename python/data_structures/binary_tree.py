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

    def find_maximum_value(self): # need to edit this
        if not self.root:
            return None
        
        return self.find_maximum_value_recursive(self.root)
    
    def find_maximum_value_recursive(self, node):
        if not node:
            return float('-inf')
        
        left_max = self.find_maximum_value_recursive(node.left)
        right_max = self.find_maximum_value_recursive(node.right)

        return max(node.value, left_max, right_max)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
