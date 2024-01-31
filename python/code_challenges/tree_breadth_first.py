from data_structures.binary_tree import BinaryTree


def breadth_first(tree):
    result = []
    if not tree.root:
        return result

    queue = [tree.root]

    while queue:
        current_node = queue.pop(0)
        result.append(current_node.value)

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

    return result
