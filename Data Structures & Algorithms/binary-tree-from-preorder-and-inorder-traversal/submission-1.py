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
        
        mapInOrder = {}
        for idx, value in enumerate(inorder):
            mapInOrder[value] = idx
        
        def dfs(left, right):

            if left > right:
                return None
            
            val = preorder[self.index]
            self.index += 1

            inOrderIndex = mapInOrder[val]
            node = TreeNode(val)

            node.left = dfs(left, inOrderIndex - 1)
            node.right = dfs(inOrderIndex + 1, right)


            return node

        return dfs(0, len(inorder) - 1)
                
