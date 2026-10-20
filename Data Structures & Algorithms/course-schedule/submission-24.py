class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        if not prerequisites:
            return True

        graph = {i: [] for i in range(numCourses)}

        for a, b in prerequisites:
            graph[b].append(a)
        
        visit = set()
        def dfs(course):

            if course in visit:
                return False

            if graph[course] == []:
                return True

            visit.add(course)
            
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False

            visit.remove(course)
            graph[course] = []

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True