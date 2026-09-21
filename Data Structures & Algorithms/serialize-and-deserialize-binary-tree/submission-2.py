# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    def __init__(self):
        self.index = 0

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        tree = []

        def dfs(node):
            if not node:
                tree.append("N")
                return

            tree.append(str(node.val))

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(tree)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        string = data.split(",")

        def dfs():
            if string[self.index] == "N":
                self.index += 1
                return None
            
            node = TreeNode(int(string[self.index]))
            self.index += 1

            node.left = dfs()
            node.right = dfs()
            
            return node

        return dfs()


