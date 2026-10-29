class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        graph = {}

        def dfs(node, target, visit):
            if node == target:
                return True
            visit.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visit:
                    if dfs(neighbor, target, visit):
                        return True

            return False

        for u, v in edges:
            if u in graph and v in graph:
                visit = set()
                if dfs(u, v, visit):
                    return [u, v]  # Encontramos un ciclo, esta es la conexión redundante

            # 2. Si no están conectados, añadimos la arista al grafo
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []

            graph[u].append(v)
            graph[v].append(u)

        
            
