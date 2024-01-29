from data_structures.binary_tree import BinaryTree


class BinarySearchTree(BinaryTree):
    """
    Put docstring here
    """

    def __init__(self):
        super().__init__()

    def add(self, value):
        self.root = self._add_recursive(self.root, value)

    def _add_recursive(self, node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._add_recursive(node.left, value)
        elif value > node.value:
            node.right = self._add_recursive(node.right, value)
        return node

    def contains(self, value):
        return self._contains_recursive(self.root, value)

    def _contains_recursive(self, node, value):
        if node is None:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._contains_recursive(node.left, value)
        else:
            return self._contains_recursive(node.right, value)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None