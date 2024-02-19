import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable


def test_set_key_value():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    assert hashtable.get("apple") == "Used for apple sauce"

def test_retrieve_by_key():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    assert hashtable.get("apple") == "Used for apple sauce"

def test_return_null_for_nonexistent_key():
    hashtable = Hashtable()
    with pytest.raises(KeyError):
        hashtable.get("nonexistent_key")

def test_list_all_unique_keys():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    hashtable.set("banana", "Yellow fruit")
    assert set(hashtable.keys()) == {"apple", "banana"}

def test_handle_collision():
    hashtable = Hashtable(size=1)  # Force collision by setting a small size
    hashtable.set("apple", "Used for apple sauce")
    hashtable.set("papel", "Not a real word")
    assert hashtable.get("apple") == "Used for apple sauce"
    assert hashtable.get("papel") == "Not a real word"

def test_retrieve_value_from_collision_bucket():
    hashtable = Hashtable(size=1)  # Force collision by setting a small size
    hashtable.set("apple", "Used for apple sauce")
    hashtable.set("papel", "Not a real word")
    assert hashtable.get("papel") == "Not a real word"

def test_hash_key_to_in_range_value():
    hashtable = Hashtable()
    key = "apple"
    hash_value = hashtable.hash(key)
    assert 0 <= hash_value < hashtable.size
