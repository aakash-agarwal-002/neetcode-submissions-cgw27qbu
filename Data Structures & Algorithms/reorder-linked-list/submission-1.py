# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        first = head
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        curr = slow.next
        prev = slow.next = None
        
        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        
        second = prev

        dummy = ListNode()
        tail = dummy

        while second:
            tail.next = first
            tail = tail.next
            first = first.next
            tail.next = second
            second = second.next
            tail = tail.next

        if first:
            tail.next = first
