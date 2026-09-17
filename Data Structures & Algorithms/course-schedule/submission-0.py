class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # 1. Create the adjancency list
        adj = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        # SEt for nodes in the current path (detect ciclycs)
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            
            if adj[crs] == []:
                return True
            
            visiting.add(crs)

            for pre in adj[crs]:
                if not dfs(pre):
                    return False
            
            visiting.remove(crs)
            adj[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
            
        return True