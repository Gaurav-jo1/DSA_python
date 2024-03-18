class Heap:
    def __init__(self, min_heap=True):
        self.heap_list = []
        self.min_heap = min_heap  # True for min-heap, False for max-heap

    # Helper function to get parent index
    def parent_idx(self, i):
        return (i - 1) // 2

    # Helper function to get left child index
    def left_child_idx(self, i):
        return 2 * i + 1

    # Helper function to get right child index
    def right_child_idx(self, i):
        return 2 * i + 2

    # Helper function to swap elements
    def swap(self, i, j):
        self.heap_list[i], self.heap_list[j] = self.heap_list[j], self.heap_list[i]

    # Heapify function to maintain heap property after insertion/deletion
    def heapify(self, i):
        left_child = self.left_child_idx(i)
        right_child = self.right_child_idx(i)
        largest_smallest = i

        # Check for left child and update largest/smallest if needed
        if left_child < len(self.heap_list) and (
            self.heap_list[left_child] > self.heap_list[largest_smallest]
            if self.min_heap
            else self.heap_list[left_child] < self.heap_list[largest_smallest]
        ):
            largest_smallest = left_child

        # Check for right child and update largest/smallest if needed
        if right_child < len(self.heap_list) and (
            self.heap_list[right_child] > self.heap_list[largest_smallest]
            if self.min_heap
            else self.heap_list[right_child] < self.heap_list[largest_smallest]
        ):
            largest_smallest = right_child

        # Swap if largest/smallest is not the current element and heapify again
        if largest_smallest != i:
            self.swap(i, largest_smallest)
            self.heapify(largest_smallest)

    # Insert element into the heap
    def insert(self, val):
        self.heap_list.append(val)
        # Start heapifying at the last inserted element (end of list)
        i = len(self.heap_list) - 1
        while i > 0 and (
            self.heap_list[i] < self.heap_list[self.parent_idx(i)]
            if self.min_heap
            else self.heap_list[i] > self.heap_list[self.parent_idx(i)]
        ):
            self.swap(i, self.parent_idx(i))
            i = self.parent_idx(i)

    # Extract the root element (minimum/maximum) from the heap
    def extract(self):
        if len(self.heap_list) == 0:
            return None
        root = self.heap_list[0]
        # Replace root with the last element and heapify down
        self.heap_list[0] = self.heap_list.pop()
        self.heapify(0)
        return root

    # Get the minimum/maximum element of the heap
    def peek(self):
        if len(self.heap_list) == 0:
            return None
        return self.heap_list[0]

    # Check if the heap is empty
    def is_empty(self):
        return len(self.heap_list) == 0


# Example usage
heap = Heap(min_heap=True)  # Create a min-heap
heap.insert(5)
heap.insert(3)
heap.insert(8)
heap.insert(1)

print(heap.extract())  # Output: 1
print(heap.peek())  # Output: 3
