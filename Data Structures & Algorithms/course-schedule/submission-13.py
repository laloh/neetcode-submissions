class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        graph = {i: [] for i in range(numCourses)}
        visited = set()

        for crs, preq in prerequisites:
            graph[crs].append(preq)

        def dfs(graph, crs):

            if crs in visited:
                return False

            if graph[crs] == []:
                return True
            
            visited.add(crs)

            for preq in graph[crs]:
                if not dfs(graph, preq):
                    return False
            
            visited.remove(crs)
            graph[crs] = []

            return True

        for crs in range(numCourses):
            if not dfs(graph, crs):
                return False
        
        return True
        