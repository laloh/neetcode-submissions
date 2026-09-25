class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)
        
        res = []
        while k > 0:
            value = -heapq.heappop(heap)
            res.append(value)
            k -= 1
        
        return res[-1]
    