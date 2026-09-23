# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.cnt = 0

    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return self.cnt
        
        def dfs(node, max_value):
            if not node:
                return 0

            if node.val >= max_value:
                self.cnt += 1

            max_value = max(max_value, node.val)

            right = dfs(node.right, max_value)
            left = dfs(node.left, max_value)
    
            return node.val

        dfs(root, root.val)
        return self.cnt