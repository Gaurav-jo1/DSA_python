class Node():
    def __init__(self, data:int):
        self.data = data
        self.next = None

class Linked_list():
    def __init__(self):
        self.head = None
        self.tail = None

    def append_end(self, data:int):
        node = Node(data)

        if not self.head:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = node

    def append_start(self, data:int):
        node = Node(data)

        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def append_index(self, data:int, index:int):
        node = Node(data)
        current_node = self.head

        if index == 0:
            return self.append_start(data)

        for i in range(1, index + 1):
            if i == index:
                node.next = current_node.next
                current_node.next = node
                return node

            current_node = current_node.next

    def delete_first(self):
        self.head = self.head.next
        return self.head

    def display_list(self):

        current = self.head

        while current.next is not None:
            print(f"{current.data} ->", end=" ")
            current = current.next

        print(f"{current.data}")

        print(f"Head - {self.head.data}")
        print(f"Tail - {self.tail.data}")

my_linked_list = Linked_list()

my_linked_list.append_end(1)
my_linked_list.append_end(2)
my_linked_list.append_end(3)
my_linked_list.append_end(4)
my_linked_list.append_end(5)

my_linked_list.append_start(0)
my_linked_list.append_start(-1)

my_linked_list.append_index(7, 5)

my_linked_list.delete_first()

my_linked_list.display_list()
