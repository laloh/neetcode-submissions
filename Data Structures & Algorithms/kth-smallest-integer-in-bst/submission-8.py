# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.kth_value = 0
        self.k = 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        if not root:
            return None
        
        self.k = k
        self.dfs(root)
        
        return self.kth_value

    def dfs(self, node):
        if not node:
            return 0

        self.dfs(node.left) 
        
        self.k -= 1
        if self.k == 0:
            self.kth_value = node.val

        self.dfs(node.right)