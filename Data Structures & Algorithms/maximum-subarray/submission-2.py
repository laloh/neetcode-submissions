class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        2 
        """

        if len(nums) == 1:
            return nums[0]

        total_sum = 0
        largest_sum = nums[0]
        for num in nums:

            total_sum += num

            largest_sum = max(largest_sum, total_sum)
            
            if total_sum < 0:
                total_sum = 0 
            
        
        return largest_sum