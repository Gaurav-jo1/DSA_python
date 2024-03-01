class Node:
    def __init__(self, data: int):
        self.prev = None
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_end(self, data):
        node = Node(data)

        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            return node

    def append_start(self, data):
        node = Node(data)

        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
            return node

    def display_list(self):

        current = self.head

        while current.next is not None:
            print(f"{current.data} ->", end=" ")
            current = current.next

        print(f"{current.data} -> End")

    def display_list_rev(self):
        current = self.tail

        while current.prev is not None:
            print(f"{current.data} ->", end=" ")
            current = current.prev

        print(f"{self.head.data} -> Start")

        print(f"Head - {self.head.data}")
        print(f"Tail - {self.tail.data}")


my_linked_list = LinkedList()

my_linked_list.append_end(1)
my_linked_list.append_end(2)
my_linked_list.append_end(3)

my_linked_list.append_start(0)

my_linked_list.display_list()
my_linked_list.display_list_rev()
