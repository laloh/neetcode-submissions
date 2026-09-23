# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()

            if node:

                if  node.val > p.val and node.val > q.val:
                    queue.append(node.left)
                elif node.val < p.val and node.val < q.val:
                    queue.append(node.right)
                else:
                    return node
        
        return None