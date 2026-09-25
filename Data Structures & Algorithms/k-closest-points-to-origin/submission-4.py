class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        if len(points) == 1:
            return points[0]
        
        heap = []
        distances = []
        for point in points:
            x, y = point[0], point[1]
            dist = math.sqrt(x*x + y*y)
            heapq.heappush(heap, (dist, [x, y]))
       
        res = []
        while k > 0:
            dist, point = heapq.heappop(heap)
            x, y  = point
            res.append([x, y])
            k -= 1

        print(res)
        return res
        