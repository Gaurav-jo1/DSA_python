class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


class Recursive_LL:
    def __init__(self):
        self.head = None

    def insertion(
        self, data: int, index: int, current_node=None, current_index: int = 0
    ):
        current_node = self.head if current_node is None else current_node.next

        if index == 0 and self.head is None:
            self.head = Node(data)
            return self.head

        elif index == 0 and self.head:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return self.head

        elif current_index + 1 == index:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
            return current_node
        else:
            return self.insertion(data, index, current_node, current_index + 1)

    def display(self):
        current = self.head

        while current:
            print(f"{current.data}", end=" -> ")
            current = current.next

        print("END")


add_node = Recursive_LL()
add_node.insertion(3, 0)
add_node.insertion(5, 1)
add_node.insertion(9, 2)
add_node.insertion(1, 3)
add_node.insertion(7, 3)

add_node.display()
