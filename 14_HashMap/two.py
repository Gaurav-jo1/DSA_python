class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, key, value):
        new_node = Node(key, value)
        new_node.next = self.head
        self.head = new_node

    def find_node(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current
            current = current.next
        return None

class HashMap:
    def __init__(self, size):
        self.size = size
        self.map = [None] * size

    def _hash_function(self, key):
        return hash(key) % self.size

    def add_item(self, key, value):
        index = self._hash_function(key)
        if self.map[index] is None:
            self.map[index] = LinkedList()

        linked_list = self.map[index]
        existing_node = linked_list.find_node(key)

        if existing_node:
            existing_node.value = value
        else:
            linked_list.add_node(key, value)

    def get_item(self, key):
        index = self._hash_function(key)
        if self.map[index] is not None:
            linked_list = self.map[index]
            node = linked_list.find_node(key)
            if node:
                return node.value
        return None

# Example usage:
hash_map = HashMap(size=10)
hash_map.add_item("key1", "value1")
hash_map.add_item("key2", "value2")

print(hash_map.get_item("key1"))  # Output: value1
print(hash_map.get_item("key2"))  # Output: value2
print(hash_map.get_item("key3"))  # Output: None
