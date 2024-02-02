from data_structures.binary_tree import BinaryTree


def fizz_buzz_tree(tree):
    def fizz_buzz_recursive(node):
        if not node:
            return None

        value = node.value

        if value % 3 == 0 and value % 5 == 0:
            node.value = "FizzBuzz"
        elif value % 3 == 0:
            node.value = "Fizz"
        elif value % 5 == 0:
            node.value = "Buzz"
        else:
            node.value = str(value)

        for child in node.children:
            fizz_buzz_recursive(child)

    # Clone the input tree to avoid modifying the original tree
    cloned_tree = tree.clone()

    fizz_buzz_recursive(cloned_tree.root)

    return cloned_tree
