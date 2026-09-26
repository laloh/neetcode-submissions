# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.max_value = 0
        self.cnt = 0

    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(node, max_value):
            if not node:
                return
            
            if node.val >= max_value:
                max_value = node.val
                self.cnt += 1

            dfs(node.left, max_value)
            dfs(node.right, max_value)

        
        dfs(root, root.val)
        return self.cnt