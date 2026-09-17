class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort()

        def backtrack(current_sum, current_list, i):
            if current_sum == target:
                if current_list not in res:
                    res.append(current_list[:])
                return
            
            if i >= len(candidates) or current_sum > target:
                return
            
            current_list.append(candidates[i])
            backtrack(current_sum + candidates[i], current_list, i+1)
            current_list.pop()
            
            next_index = i + 1
            while next_index < len(candidates) and candidates[next_index] == candidates[i]:
                next_index += 1
            backtrack(current_sum, current_list, next_index)

        backtrack(0, [], 0)
        return res