# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.kth_val = 0
        self.cnt = 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            
            self.cnt += 1
            if k == self.cnt:
                self.kth_val = node.val
            
            dfs(node.right)

        dfs(root)
        return self.kth_val
