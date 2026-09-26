# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.index = 0

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        inorderMap = {}
        for i, value in enumerate(inorder):
            inorderMap[value] = i
        
        def build(left, right):
            if left > right:
                return None

            val = preorder[self.index]
            divisionPoint = inorderMap[val]
            node = TreeNode(val)
            self.index += 1

            node.left = build(left, divisionPoint - 1)
            node.right = build(divisionPoint + 1, right)

            return node
        
        return build(0, len(preorder) - 1)
