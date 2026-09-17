# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.kth_small = []

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None

        self.dfs(root)
        return self.kth_small[k-1]

    def dfs(self, node):
        if not node:
            return 0

        self.dfs(node.left) 
        self.kth_small.append(node.val)
        self.dfs(node.right)
        