import pytest
from code_challenges.hashtable_left_join import left_join


def test_exists():
    assert left_join

    synonyms = {
        "diligent": "employed",
        "fond": "enamored",
        "guide": "usher",
        "outfit": "garb",
        "wrath": "anger",
    }
    antonyms = {
        "diligent": "idle",
        "fond": "averse",
        "guide": "follow",
        "flow": "jam",
        "wrath": "delight",
    }

    expected = [
        ["diligent", "employed", "idle"],
        ["fond", "enamored", "averse"],
        ["guide", "usher", "follow"],
        ["outfit", "garb", "NONE"],
        ["wrath", "anger", "delight"],
    ]

    actual = left_join(synonyms, antonyms)
    # Sort the lists for comparison
    expected.sort()
    actual.sort()

    assert actual == expected


def test_left_join_with_missing_synonyms():
    synonyms = {
        "happy": "joyful",
        "sad": "unhappy",
    }
    antonyms = {
        "angry": "calm",
        "sad": "happy",
    }

    expected = [
        ["angry", "calm", "NONE"],
        ["happy", "joyful", "NONE"],
        ["sad", "unhappy", "happy"],
    ]

    actual = left_join(synonyms, antonyms)
    # Sort the lists for comparison
    expected.sort()
    actual.sort()

    assert actual == expected


def test_left_join_with_empty_inputs():
    synonyms = {}
    antonyms = {}

    expected = []

    actual = left_join(synonyms, antonyms)

    assert actual == expected
