from data_structures.hashtable import Hashtable


def left_join(synonyms, antonyms):
    """
    LEFT JOINs two hashmaps into a single data structure.

    :param synonyms: Hashmap with word strings as keys and synonyms as values.
    :param antonyms: Hashmap with word strings as keys and antonyms as values.
    :return: List of lists representing the result of the LEFT JOIN operation.
    """
    result = []
    # Use sorted keys for consistency
    for key in sorted(synonyms.keys()):
        row = [key, synonyms[key]]
        if key in antonyms:
            row.append(antonyms[key])
        else:
            row.append("NONE")
        result.append(row)
    return result
