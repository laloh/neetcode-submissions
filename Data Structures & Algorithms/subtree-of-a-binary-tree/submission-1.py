# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return False

        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()

            if node:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            if self.dfs(node, subRoot):
                return True
        
        return False
    
    def dfs(self, node, subRoot):
        if not node and not subRoot:
            return True
        
        if (not node or not subRoot) or (node.val != subRoot.val):
            return False
        
        return self.dfs(node.left, subRoot.left) and self.dfs(node.right, subRoot.right)
        
