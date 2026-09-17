class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        def backtrack(current_list, i):
            
            if i >= len(nums):
                res.append(current_list.copy())
                return
            
            current_list.append(nums[i])
            backtrack(current_list, i + 1)
            current_list.pop()
            backtrack(current_list, i + 1)

        backtrack([], 0)
        return res
