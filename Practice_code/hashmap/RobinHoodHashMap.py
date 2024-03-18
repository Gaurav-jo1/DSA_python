class RobinHoodHashMap:
    def __init__(self, size=10):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def _hash_function(self, key):
        return hash(key) % self.size

    def _robin_hood_insert(self, key, value):
        hashed_key = self._hash_function(key)
        distance = 0

        while distance < self.size:
            index = (hashed_key + distance) % self.size

            if self.keys[index] is None:
                self.keys[index] = key
                self.values[index] = value
                return
            elif self.keys[index] == key:
                self.values[index] = value
                return
            elif distance < self._get_distance(self.keys[index], index):
                self.keys[index], key = key, self.keys[index]
                self.values[index], value = value, self.values[index]
            
            distance += 1
        
        raise Exception("Hashmap is full")

    def _get_distance(self, key, index):
        hashed_key = self._hash_function(key)
        if index >= hashed_key:
            return index - hashed_key
        else:
            return self.size - hashed_key + index

    def add(self, key, value):
        self._robin_hood_insert(key, value)

    def get(self, key):
        hashed_key = self._hash_function(key)
        distance = 0

        while distance < self.size:
            index = (hashed_key + distance) % self.size

            if self.keys[index] == key:
                return self.values[index]
            elif self.keys[index] is None:
                raise KeyError("Key not found in the hashmap")
            
            distance += 1
        
        raise KeyError("Key not found in the hashmap")

# Example usage:
hash_map = RobinHoodHashMap()
hash_map.add("apple", 10)
hash_map.add("banana", 20)
hash_map.add("cherry", 30)

print(hash_map.get("banana"))  # Output: 20
