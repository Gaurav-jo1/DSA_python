# When to use segment - When you query on a range.
# Perform query on a range in 
# log (n) - time complexity
# Example - Sum, Max, Avg, Min, Product.

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (2 * self.n)
        self.build_tree(arr)

    def build_tree(self, arr):
        for i in range(self.n):
            self.tree[self.n + i] = arr[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index, value):
        index += self.n
        self.tree[index] = value
        while index > 1:
            index //= 2
            self.tree[index] = self.tree[2 * index] + self.tree[2 * index + 1]

    def query(self, left, right):
        left += self.n
        right += self.n
        result = 0
        while left < right:
            if left % 2 == 1:
                result += self.tree[left]
                left += 1
            if right % 2 == 1:
                right -= 1
                result += self.tree[right]
            left //= 2
            right //= 2
        return result

# Example usage
arr = [1, 3, 5, 7, 9, 11]
segment_tree = SegmentTree(arr)
print(segment_tree.query(1, 3))  # Query the sum of elements from index 1 to 3
segment_tree.update(2, 10)  # Update the element at index 2 to 10
print(segment_tree.query(1, 3))  # Query the sum after the update
