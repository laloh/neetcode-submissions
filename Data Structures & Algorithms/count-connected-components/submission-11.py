class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = {i:[] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)


        visit = set()
        def dfs(node):
            visit.add(node)

            for neighbor in graph[node]:
                if neighbor not in visit:
                    dfs(neighbor)
            
        count = 0
        for node in range(n):
            if node not in visit:
                count += 1
                dfs(node)
        
        return count