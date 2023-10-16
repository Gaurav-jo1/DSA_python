# Leetcode question
# Link -> https://leetcode.com/problems/linked-list-cycle/

# Fast and slow pointer
# 1. Cycle detection
# 2. Node detection

# Take two pointer's starting from head, fast and slow

# Find the cycle:


def hasCycle(head=None) -> bool:
    fast_node = head
    slow_node = head

    while fast_node is not None and fast_node.next is not None:
        fast_node = fast_node.next.next
        slow_node = slow_node.next

        if fast_node == slow_node:
            return True

    return False


# Find the length


def lengthCycle(head=None) -> bool:
    fast_node = head
    slow_node = head

    while fast_node is not None and fast_node.next is not None:
        fast_node = fast_node.next.next
        slow_node = slow_node.next

        if fast_node == slow_node:
            temp = slow_node
            length = 0
            while True:
                temp = temp.next
                length += 1
                if temp == slow_node:
                    break

    return 0
    
    
