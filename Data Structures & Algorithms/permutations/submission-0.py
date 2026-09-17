class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtracking(perm):

            if len(perm) == len(nums):
                res.append(perm[:])
                return
            
            for n in nums:
                if n in perm:
                    continue
                
                perm.append(n)
                backtracking(perm)
                perm.pop()


        backtracking([])
        return res