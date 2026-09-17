# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        uniqueList = []
        for l in lists:
            if l:
                head = l
                while head:
                    uniqueList.append(head.val)
                    head = head.next

        dummy = ListNode()
        head = dummy
        for value in sorted(uniqueList):
            dummy.next = ListNode(val=value)
            dummy = dummy.next
        
        dummy.next = None
        
        return head.next