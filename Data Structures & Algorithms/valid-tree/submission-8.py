class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n - 1:
            return False

        adjList = {i:[] for i in range(n)}
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)

            for child in adjList[node]:
                if child == parent:
                    continue

                if not dfs(child, node):
                    return False

            return True

        if not dfs(0, -1):
            return False

        return len(visited) == n