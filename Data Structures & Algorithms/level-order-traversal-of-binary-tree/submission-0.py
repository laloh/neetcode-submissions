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

        queue.append(root)
        res = [[root.val]]
        while queue:
            currLevel = []
            for _ in range(len(queue)):
                currentNode = queue.popleft()

                if currentNode and currentNode.left:
                    queue.append(currentNode.left)
                    currLevel.append(currentNode.left.val)

                if currentNode and currentNode.right:
                    queue.append(currentNode.right)
                    currLevel.append(currentNode.right.val)
            
            if currLevel:
                res.append(currLevel)
        
        return res
