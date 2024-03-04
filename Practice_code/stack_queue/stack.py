import sys

class Stack():

    def __init__(self) -> None:
        self.items = []

    def push(self, data):
        self.items.append(data)
        return self.items
    
    def peek(self):
        if self.is_empty():
            print("The List is Empty")
        else:
            return self.items[-1]
    
    def pop(self):
        if self.is_empty():
            print("The List is Empty")
        else:
            self.items.pop()
            return self.items
    
    def is_empty(self) -> bool:
        if self.size()  == 0:
            return True
        else:
            return False
        
    def size(self):
        return len(self.items)


# Example usage

stack = Stack()

# Pushing elements onto the stack
stack.push(5)
stack.push(10)
stack.push(15)

# Peeking at the top element
print("Top element:", stack.peek())

# # Popping elements from the stack
print("Popped:", stack.pop())
# print("Popped:", stack.pop())

# # Checking if the stack is empty
print("Is the stack empty:", stack.is_empty())

# # Size of the stack
print("Size of the stack:", stack.size())