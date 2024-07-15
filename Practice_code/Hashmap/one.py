class HashMap:
    
    def __init__(self, capacity=10) -> None:
        self.capacity = capacity
        self.bucket = [[] for _ in range(self.capacity)]
        
    def hash(self, key):
        return hash(key) % self.capacity
        
    def put(self, key, value):
        index = self.hash(key)
        bucket = self.bucket[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
    
    def __str__(self) -> str:
        hashmap_str = ""
        
        for i, b in enumerate(self.bucket):
            hashmap_str += f"Bucket {i}: {b}\n"
            
        return hashmap_str
    
hashmap = HashMap()
hashmap.put("key1", "value1")
hashmap.put("key2", "value2")
hashmap.put("key3", "value3")
print(hashmap)