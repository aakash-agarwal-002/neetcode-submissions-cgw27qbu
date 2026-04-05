# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # find mid
        slow = head
        fast = head.next
        list1 = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse second half
        current = slow.next
        prev = slow.next = None

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        list2 = prev

        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            tail.next = list1
            list1 = list1.next
            tail = tail.next
            tail.next = list2
            tail = tail.next
            list2 = list2.next
        
        if list1:
            tail.next = list1
        


        
        




        
        

        
