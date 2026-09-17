class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        2 
        """

        total_sum = 0
        largest_sum = nums[0]
        for num in nums:
            if total_sum < 0:
                total_sum = 0 

            total_sum += num

            largest_sum = max(largest_sum, total_sum)
     
        
        return largest_sum