# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if (not head) or (head and not head.next):
            return False

        slow = head
        faster = head.next

        while faster and faster.next:

            if slow == faster:
                return True

            slow = slow.next
            faster = faster.next.next

        return False