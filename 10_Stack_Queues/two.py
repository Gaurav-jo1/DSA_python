class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise Exception('Deque is empty.')

    def remove_rear(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise Exception('Deque is empty.')

    def size(self):
        return len(self.items)


# Example usage
deque = Deque()

# Adding elements to the deque
deque.add_front(5)
deque.add_rear(10)
deque.add_front(15)

# Removing elements from the deque
print("Removed from front:", deque.remove_front())
print("Removed from rear:", deque.remove_rear())

# Checking if the deque is empty
print("Is the deque empty:", deque.is_empty())

# Size of the deque
print("Size of the deque:", deque.size())
