class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        # intervals.sort()

        res = []
        for qry in queries:
            heap = []
            for itv in intervals:
                if  itv[0] <= qry <= itv[1]:
                    heapq.heappush(heap, itv[1] - itv[0] + 1)
            
            
            if heap:
                res.append(heapq.heappop(heap))
            else:
                res.append(-1)
        
        return res
