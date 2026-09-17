# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length = 0
        tmp = head
        while tmp:
            length += 1
            tmp = tmp.next

        idx = length - n
        if idx == 0:
            return head.next

        node = head
        i = 0
        prev = None
        while node and i != idx:
            if i == idx - 1:
                prev = node

            node = node.next
            i += 1
        
        _next = None
        if node.next:
            _next = node.next
        
        prev.next = _next
    
        return head