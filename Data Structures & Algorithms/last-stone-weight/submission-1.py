import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        max_heap = [-value for value in stones]
        heapq.heapify(max_heap)
        
        while len(max_heap) > 1:

            first, second = -heapq.heappop(max_heap), -heapq.heappop(max_heap)

            if first != second:
                _diff = abs(first - second)
                heapq.heappush(max_heap, -_diff)
            

        return -max_heap[0] if max_heap else 0