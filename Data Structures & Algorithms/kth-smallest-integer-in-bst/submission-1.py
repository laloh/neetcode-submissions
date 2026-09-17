# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.count = 0
        self.min_value = 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.dfs(root, k)
        return self.min_value
    
    def dfs(self, root, k):

        if not root:
            return 0
        
        self.dfs(root.left, k)

        self.count += 1
        if self.count == k:
            self.min_value = root.val

        print(root.val, self.count)

        self.dfs(root.right, k)

