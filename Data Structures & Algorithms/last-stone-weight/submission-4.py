class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        """
        [2, 3, 6, 2, 4]
        heapify
        [6, 4, 3, 2, 2]

        6 vs 4 -> 2
        [3, 2, 2, 2]
        
        3 vs 2 -> 1
        [2, 2, 1]

        2 v 2  -> None
        [1]


        """

        if len(stones) < 2:
            return stones[0]

        heap = []
        for stn in stones:
            heapq.heappush(heap, -stn)
        
        print(heap)
        while heap:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)
            crash = abs(x-y)
            
            print(crash)
            if crash >= 1:
                heapq.heappush(heap, -crash)

            print(heap)
            
            if len(heap) == 1:
                break
            
        return -heap[0] if heap else 0

