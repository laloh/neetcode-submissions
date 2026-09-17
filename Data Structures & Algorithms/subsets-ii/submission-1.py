class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()
        
        def backtrack(i, current_list):
            if i >= len(nums):
                res.append(current_list.copy())
                return
        
            current_list.append(nums[i])
            backtrack(i + 1, current_list)
            
            current_list.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            
            backtrack(i + 1, current_list)

        backtrack(0, [])
        return res


