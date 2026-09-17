# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        queue = deque()
        queue.append(root)

        while queue:
            
            node = queue.popleft()
            
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
            
            if self.dfs(node, subRoot):
                return True
        
        return False

    
    def dfs(self, p, q):
        if not p and not q:
            return True
        
        if not p or not q or p.val != q.val:
            return False

        return self.dfs(p.left, q.left) and self.dfs(p.right, q.right)        