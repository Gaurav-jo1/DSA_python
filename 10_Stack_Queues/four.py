class DynamicCircularQueue:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.queue = [None] * self.capacity
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        if self.is_full():
            self.resize()
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return item

    def resize(self):
        new_capacity = self.capacity * 2
        new_queue = [None] * new_capacity
        for i in range(self.capacity):
            new_queue[i] = self.queue[(self.front + i) % self.capacity]
        self.front = 0
        self.rear = self.capacity - 1
        self.capacity = new_capacity
        self.queue = new_queue

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Elements in the queue are:", end=" ")
            i = self.front
            while i != self.rear:
                print(self.queue[i], end=" ")
                i = (i + 1) % self.capacity
            print(self.queue[self.rear])


# Example usage
queue = DynamicCircularQueue(3)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.display()
queue.dequeue()
queue.enqueue(4)
queue.display()
queue.enqueue(5)
queue.enqueue(6)
queue.display()
