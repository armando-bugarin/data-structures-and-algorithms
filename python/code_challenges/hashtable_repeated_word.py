from data_structures.hashtable import Hashtable


def first_repeated_word(input_string):
    words = input_string.split()
    hashtable = Hashtable()

    for word in words:
        # Remove punctuation and convert to lowercase
        cleaned_word = ''.join(e for e in word if e.isalnum()).lower()

        # Check if the word already exists in the hashtable
        if hashtable.has(cleaned_word):
            return cleaned_word
        else:
            hashtable.set(cleaned_word, True)

    return None
