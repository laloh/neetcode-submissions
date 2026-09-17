# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def __init__(self):
        self.arr = []
        self.kthValue = 0
        self.cnt = 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # n 
        self.dfs(root, k)
    
        # decrement by 1, because index starts in 0
        return self.kthValue
    
    def dfs(self, root, k):
        if not root:
            return 0
        
        self.dfs(root.left, k)
        
        self.cnt += 1
        print(self.cnt, root.val)
        if k == self.cnt:
            self.kthValue = root.val
    
        self.dfs(root.right, k)
