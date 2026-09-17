class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def backtrack(current_sum, current_list, i):

            if current_sum == target:
                res.append(current_list[:])
                return
            
            if i >= len(nums) or current_sum > target:
                return
            
            current_list.append(nums[i])
            backtrack(current_sum + nums[i], current_list, i)
            current_list.pop()
            backtrack(current_sum, current_list, i+1)

        
        backtrack(0, [], 0)
        return res