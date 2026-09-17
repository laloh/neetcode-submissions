class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []

        def dfs(subset, i):

            _sum = sum(subset)


            if _sum == target:
                res.append(subset.copy())
                return
        
            if i >= len(nums) or sum(subset) > target:
                return

            subset.append(nums[i])
            dfs(subset, i)
            subset.pop()
            dfs(subset, i+1)
        
        dfs([], 0)
        return res


