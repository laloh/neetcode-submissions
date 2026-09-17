class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        hm = {}
        
        def backtrack(i, current_list):

            if i >= len(nums):
                cl_copy = sorted(current_list[:])
                hm[str(cl_copy)] = cl_copy
                return
            
            current_list.append(nums[i])
            backtrack(i + 1, current_list)
            current_list.pop()

            backtrack(i+1, current_list)
        
        backtrack(0, [])
        
        return [l for k, l in hm.items()]