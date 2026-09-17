class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        res = []
        _map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(i, current_str):

            if len(current_str) == len(digits):
                res.append("".join(current_str))
                return
            
            # if i > len(digits):
            #     return

            possible_chars = _map[digits[i]]
            for char in possible_chars:
                current_str.append(char)
                backtrack(i+1, current_str)
                current_str.pop()
        
        if not digits:
            return []
        
        backtrack(0, [])
        return res

