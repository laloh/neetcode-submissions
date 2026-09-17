"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        visited = {}

        def dfs(node, visited):
            
            if node in visited:
                return visited[node]
            
            cloned_node = Node(node.val)
            visited[node] = cloned_node

            for children in node.neighbors:
                cloned_children = dfs(children, visited)
                cloned_node.neighbors.append(cloned_children)
            
            return cloned_node
        
        dfs(node, visited)
        return visited[node]