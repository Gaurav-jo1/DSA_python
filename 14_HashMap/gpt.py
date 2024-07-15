class HashMap:
    def __init__(self, initial_capacity=10):
        self.capacity = initial_capacity
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]

    def hash(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        index = self.hash(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value)) 
        self.size += 1
    
    def get(self, key):
        index = self.hash(key)
        bucket = self.buckets[index]
        
        for k, v in bucket:
            if k == key:
                return v
        return None
    
    def remove(self, key):
        index = self.hash(key)
        bucket = self.buckets[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return
        return None
    
    def __str__(self):
        hashmap_str = ""
        for i, bucket in enumerate(self.buckets):
            hashmap_str += f"Bucket {i}: {bucket}\n"
        return hashmap_str

# Example usage
hash_map = HashMap()
hash_map.put("key1", "value1")
hash_map.put("key2", "value2")
print("Initial HashMap:")
print(hash_map)

print("\nGet value for 'key1':", hash_map.get("key1"))

hash_map.put("key1", "value3")
print("\nHashMap after updating 'key1':")
print(hash_map)

hash_map.remove("key2")
print("\nHashMap after removing 'key2':")
print(hash_map)
