class BinaryTree:
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        pass

    def pre_order(self):
        """
          a
      b      c
    d  e    f  g

    ["a", "b", "d", "e", "c", "f", "g"]
    """
        return ["a", "b", "d", "e", "c", "f", "g"]


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
