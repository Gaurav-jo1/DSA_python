class Node:
    def __init__(self, data: int):
        self.data = data
        self.previous = None
        self.next = None

class Doubly_LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def append_end(self, data:int):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def append_start(self, data:int):

        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

    def display(self):

        current = self.head

        while current:
            print(f"{current.data}", end= " -> ")
            current = current.next

        print("End")

    def display_rev(self):

        current = self.tail

        while current:
            print(f"{current.data}", end=" -> ")
            current = current.previous

        print("Start")

my_list = Doubly_LinkedList()
my_list.append_end(3) 
my_list.append_end(4) 
my_list.append_end(5) 
my_list.display_rev()