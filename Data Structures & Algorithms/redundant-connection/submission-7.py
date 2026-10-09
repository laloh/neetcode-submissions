class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        graph = {}

        def dfs(node, target, visited):
            if node == target:
                return True
            
            visited.add(node)

            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    if dfs(neighbor, target, visited):
                        return True

            return False

        for u, v in edges:
            # Si ambos nodos ya están en el grafo, verificamos si hay un camino de u a v
            if u in graph and v in graph:
                visited = set()
                if dfs(u, v, visited):
                    return [u, v]
            
            # Si no hay ciclo, agregamos la arista al grafo no dirigido
            graph.setdefault(u, []).append(v)
            graph.setdefault(v, []).append(u)
        
        return []

