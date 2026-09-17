# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
         0 -> 1 -> 2 -> 3

        None <- 0 <- 1 <- 2 

        head = 0, 1
        prev = None, 1, 2

        """

        if not head:
            return None

        prev = None
        while head and head.next:
            _next = head.next
            head.next = prev
            prev = head
            head = _next
        
        head.next = prev

        return head

