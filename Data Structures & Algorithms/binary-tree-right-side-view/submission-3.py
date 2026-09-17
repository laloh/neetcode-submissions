# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque

        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        res = []

        while queue:
            sizeQueue = len(queue)
            for i in range(sizeQueue):
                node = queue.popleft()

                if i == sizeQueue - 1:
                    res.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return res

