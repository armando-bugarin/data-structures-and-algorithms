from data_structures.binary_tree import BinaryTree


def tree_intersection(tree_a, tree_b):
    """
    Find common values in two binary trees.
    """
    values_a = set(tree_a.in_order())
    values_b = set(tree_b.in_order())
    
    common_values = values_a.intersection(values_b)
    return list(common_values)
