# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(node, max_value):
            if not node:
                return 0
            
            count = 0
            if node.val >= max_value:
                max_value = node.val
                count += 1

            count += dfs(node.left, max_value)
            count += dfs(node.right, max_value)

            return count
            
        return dfs(root, root.val)
        