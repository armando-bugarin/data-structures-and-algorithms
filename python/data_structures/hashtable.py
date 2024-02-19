class Hashtable:
    """
    Put docstring here
    """

    def __init__(self, size=1024):
        self.size = size
        self._buckets = [None] * self.size

    def hash(self, key):
        """
        Hashes the key and returns an index in the collection for that key.
        """
        hash_value = 0
        for char in str(key):
            hash_value += ord(char)
        return hash_value % self.size

    def set(self, key, value):
        """
        Hashes the key and sets the key and value pair in the table.
        Handles collisions as needed. If a given key already exists, replaces its value.
        """
        index = self.hash(key)
        if self._buckets[index] is None:
            self._buckets[index] = [[key, value]]
        else:
            for item in self._buckets[index]:
                if item[0] == key:
                    item[1] = value  # Replace value if key already exists
                    return
            self._buckets[index].append([key, value])

    def get(self, key):
        """
        Retrieves the value associated with the given key in the table.
        """
        index = self.hash(key)
        if self._buckets[index] is not None:
            for item in self._buckets[index]:
                if item[0] == key:
                    return item[1]
        raise KeyError(f"Key '{key}' not found in the hashtable")

    def has(self, key):
        """
        Checks if the key exists in the table.
        Returns a boolean indicating if the key exists.
        """
        index = self.hash(key)
        if self._buckets[index] is not None:
            for item in self._buckets[index]:
                if item[0] == key:
                    return True
        return False

    def keys(self):
        """
        Returns a collection of keys in the hashtable.
        """
        all_keys = []
        for bucket in self._buckets:
            if bucket is not None:
                all_keys.extend(item[0] for item in bucket)
        return all_keys
