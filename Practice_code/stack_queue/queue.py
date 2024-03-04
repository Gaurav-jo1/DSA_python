class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise Exception('Queue is empty.')

    def size(self):
        return len(self.items)


# Example usage

queue = Queue()

# Enqueuing elements into the queue
queue.enqueue(5)
queue.enqueue(10)
queue.enqueue(15)

# Dequeuing elements from the queue
print("Dequeued:", queue.dequeue())
print("Dequeued:", queue.dequeue())

# Checking if the queue is empty
print("Is the queue empty:", queue.is_empty())

# Size of the queue
print("Size of the queue:", queue.size())
