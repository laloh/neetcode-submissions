# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def __init__(self):
        self.arr = []

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # log n 
        self.dfs(root)
        
        # n log n 
        self.arr.sort()

        # n log n
        print(self.arr)
        
        # decrement by 1, because index starts in 0
        return self.arr[k-1]
    
    def dfs(self, root):
        if not root:
            return
        
        self.dfs(root.left)

        self.arr.append(root.val)
        
        self.dfs(root.right)