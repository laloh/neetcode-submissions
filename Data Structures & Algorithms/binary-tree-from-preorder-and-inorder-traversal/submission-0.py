# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Crear un mapa para buscar indices en inorder rapido
        mapInorder = {}
        for i in range(len(inorder)):
            mapInorder[inorder[i]] = i
        
        # Indice global para rastrear la raiz actual
        preIndex = 0
    
        def build(left, right):
            nonlocal preIndex
            if left > right:
                return None
            
            # El primer elemento disponible en preorder es la raiz
            rootValue = preorder[preIndex]
            node = TreeNode(val=rootValue)
            preIndex += 1
        
            # Buscamos donde divide la raiz al arreglo inorder
            pointDivision = mapInorder[rootValue]

            # Construimos los subarboles
            node.left = build(left, pointDivision - 1)
            node.right = build(pointDivision + 1, right)

            return node
        

        return build(0, len(inorder)-1)

        
