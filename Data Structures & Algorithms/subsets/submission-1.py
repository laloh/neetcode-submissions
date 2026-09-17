class Solution:
    def __init__(self):
        self.res = []
        self.current = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        i = 0
        self.dfs(i, nums)

        return self.res
    
    def dfs(self, i, nums):
        if i >= len(nums):
            self.res.append(self.current.copy())
            return
        
        self.current.append(nums[i])
        self.dfs(i+1, nums)

        self.current.pop()
        self.dfs(i+1, nums)
    
