class Solution:
    def countSubstrings(self, s: str) -> int:
        
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        substr_cnt = 0
        for i in range(n):
            dp[i][i] = True
            substr_cnt += 1
        
        for i in range(n - 1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                substr_cnt += 1
        
        for substr_len in range(3, n + 1):
            for i in range(n - substr_len + 1):
                j = i + substr_len - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    substr_cnt += 1

        return substr_cnt