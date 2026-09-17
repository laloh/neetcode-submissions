# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        queue = deque()

        if not root:
            return []
        
        res = []
        queue.append(root)
        while queue:
            currLevel = []
            for _ in range(len(queue)):
                currentNode = queue.popleft()
                if currentNode:
                    currLevel.append(currentNode.val)
                    queue.append(currentNode.left)
                    queue.append(currentNode.right)

            
            if currLevel:
                res.append(currLevel)
        
        return res
