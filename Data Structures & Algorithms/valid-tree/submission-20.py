class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return True

        graph = {i: [] for i in range(n)}

        for u, v in edges:
            graph[v].append(u)
            graph[u].append(v)

        visit = set()
        def dfs(parent, node):

            if node in visit:
                return False

            visit.add(node)

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue 

                if not dfs(node, neighbor):
                    return False

            return True

        if not dfs(-1, 0):
            return False

        return len(visit) == n