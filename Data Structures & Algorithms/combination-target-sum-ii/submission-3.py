class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort()
        def backtrack(current_list, current_sum, i):

            if current_sum == target:
                res.append(current_list.copy())
                return
            
            if i >= len(candidates) or current_sum > target:
                return
            
            current_list.append(candidates[i])
            backtrack(current_list, current_sum + candidates[i], i+1)

            current_list.pop()

            next_i = i + 1
            while next_i < len(candidates) and candidates[next_i] == candidates[i]:
                next_i += 1

            backtrack(current_list, current_sum, next_i) 

        backtrack([], 0, 0)
        return res
        
