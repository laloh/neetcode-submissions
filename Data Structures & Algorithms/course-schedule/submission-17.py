class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        visited = set()
        visiting = set()
        adjList = {}

        for course in range(numCourses):
            adjList[course] = []

        for a, b in prerequisites:
            if b not in adjList:
                adjList[b] = []
            adjList[b].append(a)
        

        def dfs(parent, child):
            if parent in visited:
                return False

            if child == []:
                return True

            visited.add(parent)

            for child in adjList[parent]:
                if not dfs(child, adjList[child]):
                    return False
                
            visited.remove(parent)
            adjList[parent] = []

            return True
            

        
        for parent, child_list in adjList.items():
            if not dfs(parent, child_list):
                return False
        
        return True
        