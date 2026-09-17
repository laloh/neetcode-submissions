class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) > (n - 1):
            return False

        adj = {i: [] for i in range(n)}

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = {0}
        queue = deque([0])

        while queue:
            node = queue.popleft()

            for nei in adj[node]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append(nei)
            
        
        return True if len(visited) == n else False