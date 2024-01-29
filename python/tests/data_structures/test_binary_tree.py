import pytest
from data_structures.binary_tree import BinaryTree, Node


# @pytest.mark.skip("TODO")
def test_exists():
    assert BinaryTree


# @pytest.mark.skip("TODO")
def test_pre_order(tree):
    actual = tree.pre_order()
    expected = ["a", "b", "d", "e", "c", "f", "g"]
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_in_order(tree):
    actual = tree.in_order()
    expected = ["d", "b", "e", "a", "f", "c", "g"]
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_post_order(tree):
    actual = tree.post_order()
    expected = ["d", "e", "b", "f", "g", "c", "a"]
    assert actual == expected

def test_empty_tree():
    tree = BinaryTree()
    assert tree.pre_order() == []
    assert tree.in_order() == []
    assert tree.post_order() == []

def test_single_node_tree():
    tree = BinaryTree()
    tree.root = Node("a")
    assert tree.pre_order() == ["a"]
    assert tree.in_order() == ["a"]
    assert tree.post_order() == ["a"]

def test_add_children_to_node():
    tree = BinaryTree()
    tree.root = Node("a")
    tree.root.left = Node("b")
    tree.root.right = Node("c")
    assert tree.pre_order() == ["a", "b", "c"]
    assert tree.in_order() == ["b", "a", "c"]
    assert tree.post_order() == ["b", "c", "a"]



@pytest.fixture
def tree():
    """
          a
      b      c
    d  e    f  g
    """

    tree = BinaryTree()

    tree.root = Node("a")
    tree.root.left = Node("b")
    tree.root.right = Node("c")
    tree.root.left.left = Node("d")
    tree.root.left.right = Node("e")
    tree.root.right.left = Node("f")
    tree.root.right.right = Node("g")

    return tree
