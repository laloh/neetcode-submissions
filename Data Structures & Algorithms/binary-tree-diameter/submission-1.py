# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.max_diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.dfs(root)
        return self.max_diameter



    def dfs(self, root):

        if not root:
            return 0
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        if left + right > self.max_diameter:
            self.max_diameter = left + right
        
        return max(left, right) + 1