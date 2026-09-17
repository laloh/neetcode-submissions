class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        goal = 0
        for i in range(len(nums)):

            if i > goal:
                return False
            
            goal = max(goal, i + nums[i])
            print(goal)
            if goal == len(nums) - 1:
                return True
        
        return True
