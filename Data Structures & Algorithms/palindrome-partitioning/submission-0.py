class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        part = []

        def isPali(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(i):
            if i >= len(s):
                res.append(part[:])
                return
            
            for j in range(i, len(s)):
                substr = s[i: j + 1]
                if isPali(s, i, j):
                    part.append(substr)
                    backtrack(j + 1)
                    part.pop()

        backtrack(0)
        return res