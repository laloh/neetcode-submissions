# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        """
        - Reverse both LL
        - build num for both LL
        - Do the sum
        - Build the res LL
        - Reverse the res LL
        - return Head
        """
    
        l1Rev = self.reverseLL(l1)
        l2Rev = self.reverseLL(l2)

        num1 = self.buildNumber(l1Rev)
        num2 = self.buildNumber(l2Rev)

        _sum = num1 + num2

        head = self.buildLLfromNumber(_sum)

        return head

    

    def buildLLfromNumber(self, number):
        
        _str = str(number)[::-1]
        head = ListNode(_str[0])
        node = head
        for char in _str[1:]:
            head.next = ListNode(char)
            head = head.next
        
        head.next = None

        return node
    
    def buildNumber(self, head):
        
        node = head
        num = ""
        while node:
            num += str(node.val)
            node = node.next
        
        return int(num)

    def reverseLL(self, head):
        prev = None
        node = head
        while node:
            _next = node.next
            node.next = prev
            prev = node
            node = _next
        
        test = prev
        while test:
            print(test.val)
            test = test.next
        
        return prev