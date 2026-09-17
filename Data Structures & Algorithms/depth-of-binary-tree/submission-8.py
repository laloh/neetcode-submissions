# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        stack = deque()
        if root:
            stack.append(root)
        
        lvl = 0

        while stack:

            for _ in range(len(stack)):
                node = stack.popleft()
                if node.left:
                    stack.append(node.left)
                if node.right:    
                    stack.append(node.right)
            lvl += 1

        return lvl



