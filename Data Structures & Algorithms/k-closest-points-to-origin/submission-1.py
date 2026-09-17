class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        min_heap = []

        for x, y in points:
            dist = x*x + y*y
            heapq.heappush(min_heap, (dist, x, y))
        
        res = []
        for i in range(k):
            _, x, y = heapq.heappop(min_heap)
            res.append([x,y])

        return res