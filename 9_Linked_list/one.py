# Singly Linked List
# 1. Adding new Node to the end

class Node:
    def __init__(self, data:int):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_e(self, data:int):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def append_s(self, data:int):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Creating a linked list

my_linked_list = LinkedList()

# my_linked_list.append_e(1)
# my_linked_list.append_e(2)
# my_linked_list.append_e(3)

# # Displaying the linked list

# my_linked_list.display()


# 2. Adding New Node to the start
my_linked_list.append_s(1)
my_linked_list.append_s(2)
my_linked_list.append_s(3)

my_linked_list.display()