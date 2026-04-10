class Solution:
    def removeNthFromEnd(self, head, n):
        slow = head
        fast = head

        # Move fast n steps ahead
        for _ in range(n):
            fast = fast.next

        # If fast is None → delete head
        if fast is None:
            return head.next

        # Move both pointers
        while fast.next:
            slow = slow.next
            fast = fast.next

        # Delete node
        slow.next = slow.next.next

        return head