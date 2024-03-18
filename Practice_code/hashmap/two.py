class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.map = [[] for _ in range(size)]

    def _hash_function(self, key):
        return hash(key) % self.size

    def add(self, key, value):
        hashed_key = self._hash_function(key)
        for item in self.map[hashed_key]:
            if item[0] == key:
                item[1] = value  # Update value if key already exists
                return
        self.map[hashed_key].append([key, value])

    def get(self, key):
        hashed_key = self._hash_function(key)
        for item in self.map[hashed_key]:
            if item[0] == key:
                return item[1]  # Return value if key found
        raise KeyError("Key not found in the hashmap")

    def remove(self, key):
        hashed_key = self._hash_function(key)
        for i, item in enumerate(self.map[hashed_key]):
            if item[0] == key:
                del self.map[hashed_key][i]  # Remove key-value pair
                return
        raise KeyError("Key not found in the hashmap")

# Example usage:
hash_map = HashMap()
hash_map.add("apple", 10)
hash_map.add("banana", 20)
hash_map.add("cherry", 30)

print(hash_map.get("banana"))  # Output: 20
hash_map.remove("banana")
print(hash_map.get("banana"))  # Raises KeyError: Key not found in the hashmap
