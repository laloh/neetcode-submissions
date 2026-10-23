class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        num_comp = 0

        def dfs(node):
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)
            
        for i in range(n):
            if i not in visited:
                num_comp += 1
                dfs(i)
        
        return num_comp