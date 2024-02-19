import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable


def test_set_get():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected


def test_set_replace():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    hashtable.set("apple", "New value")
    actual = hashtable.get("apple")
    expected = "New value"
    assert actual == expected


def test_has():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    assert hashtable.has("apple") is True
    assert hashtable.has("banana") is False


def test_keys():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    hashtable.set("banana", "Yellow fruit")
    actual = hashtable.keys()
    expected = ["apple", "banana"]
    assert set(actual) == set(expected)
