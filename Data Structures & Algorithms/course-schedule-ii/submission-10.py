class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adjList = {i:[] for i in range(numCourses)}
        inDegree = [0] * numCourses


        for crs, preq in prerequisites:
            adjList[preq].append(crs)
            inDegree[crs] += 1

        queue = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)

        res = []            
        while queue:
            crs = queue.popleft()
            res.append(crs)

            for preq in adjList[crs]:
                inDegree[preq] -= 1
                if inDegree[preq] == 0:
                    queue.append(preq)

        return res if len(res) == numCourses else []

