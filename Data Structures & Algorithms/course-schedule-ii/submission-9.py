class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adjList = {}

        visited = set()
        visiting = set()
        orderCourse = []

        for i in range(numCourses):
            adjList[i] = []
        
        for crs, preq in prerequisites:
            adjList[preq].append(crs)
        
        def dfs(crs):
            if crs in visiting:
                return False
            
            if crs in visited:
                return True
    
            visiting.add(crs)

            for nextCourse in adjList[crs]:
                if not dfs(nextCourse):
                    return False
        
            visiting.remove(crs)
            visited.add(crs)    
            orderCourse.append(crs)
            
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return orderCourse[::-1]