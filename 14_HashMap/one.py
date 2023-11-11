class HashMap:
    def __init__(self, size=100):
        self.size = size
        self.hashmap = [[] for _ in range(size)]

    def _hash_function(self, key):
        return hash(key) % self.size

    def add(self, key, value):
        hash_key = self._hash_function(key)
        for pair in self.hashmap[hash_key]:
            if pair[0] == key:
                pair[1] = value
                return
        self.hashmap[hash_key].append([key, value])

    def get(self, key):
        hash_key = self._hash_function(key)
        for pair in self.hashmap[hash_key]:
            if pair[0] == key:
                return pair[1]
        raise KeyError(f"Key '{key}' not found.")

    def remove(self, key):
        hash_key = self._hash_function(key)
        for i, pair in enumerate(self.hashmap[hash_key]):
            if pair[0] == key:
                del self.hashmap[hash_key][i]
                return
        raise KeyError(f"Key '{key}' not found.")

# Example usage:
my_map = HashMap()
my_map.add("name", "John")
my_map.add("age", 25)

print(my_map.get("name"))  # Output: John

my_map.add("age", 26)  # Update the value for the existing key
print(my_map.get("age"))  # Output: 26

my_map.remove("name")
# my_map.get("name")  # This line will raise a KeyError because "name" is removed

