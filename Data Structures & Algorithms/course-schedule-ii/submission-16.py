class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        if not prerequisites:
            return  [i for i in range(numCourses)] 

        graph = {i: [] for i in range(numCourses)}

        for u, v in prerequisites:
            graph[v].append(u)

        visit = set()
        def dfs(course):
            if course in visit:
                return False

            visit.add(course)
            
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False

            visit.remove(course)
            graph[course] = []
            order.append(course)
            
            return True
        
        order = []
        for course in range(numCourses):
            if not dfs(course):
                return []
            
        
        return order[::-1]