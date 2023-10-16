class Solution:
    def middleNode(self, head):
        fast = head
        slow = head

        while fast != None and fast.next != None :
            
            fast = fast.next.next
            slow = slow.next
        
        return slow
    