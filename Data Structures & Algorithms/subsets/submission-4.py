class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        res = []

        def dfs(i, nums):
            if i >= len(nums):
               res.append(subset.copy())
               return

            subset.append(nums[i])
            dfs(i + 1, nums)
            subset.pop()
            dfs(i+1, nums)

        dfs(0, nums)
        return res
