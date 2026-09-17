class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        adj = defaultdict(list)

        def dfs(node, parent):
            if node == parent:
                return True
            
            visited.add(node)

            for nei in adj[node]:
                if nei not in visited:
                    if dfs(nei, parent):
                        return True

            return False
        
        for u, v in edges:
            visited = set()
            if dfs(u, v):
                return [u, v]
            
            adj[u].append(v)
            adj[v].append(u)
