# Singly Linked List
# 1. Adding new Node to the end


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_e(self, data: int):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def append_s(self, data: int):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def append_index(self, data: int, index: int):
        new_node = Node(data)
        current_node = self.head

        if index == 0:
            return self.append_s(data)

        for i in range(1, index + 1):
            if i == index:
                new_node.next = current_node.next
                current_node.next = new_node
                return

            current_node = current_node.next

    def delete__first_node(self):
        self.head = self.head.next

    def delete_last_node(self):
        current = self.head

        while current.next:
            current_previous = current
            current = current.next

        self.tail = current_previous
        self.tail.next = None

    def delete_node_index(self, index: int):
        current = self.head

        if index == 0:
            self.delete__first_node()
            return

        for i in range(index + 1):
            if i == index:
                current_previous.next = current.next
                return

            current_previous = current
            current = current.next

            if not current:
                print("Index is Out of range")
                return

        # 1 2 3 4 5

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("End")


# Creating a linked list

my_linked_list = LinkedList()

my_linked_list.append_e(1)
my_linked_list.append_e(2)
my_linked_list.append_e(3)
my_linked_list.append_e(4)
my_linked_list.append_e(5)
# my_linked_list.append_index(3, 3)
# my_linked_list.delete__first_node()
# my_linked_list.delete_last_node()
my_linked_list.delete_node_index(10)
# Displaying the linked list

my_linked_list.display()


# 2. Adding New Node to the start
# my_linked_list.append_s(1)
# my_linked_list.append_s(2)
# my_linked_list.append_s(3)

# my_linked_list.display()

# my_linked_list.append_index(3, 0)
