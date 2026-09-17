class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]

        start_index = 0
        max_len = 1
        for i in range(n):
            dp[i][i] = True
        
        for i in range(n - 1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                start_index = i
                max_len = 2

        for substr_len in range(3, n + 1):
            for i in range(n - substr_len + 1):
                j = i + substr_len - 1

                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    max_len = substr_len
                    start_index = i
        

        return s[start_index:start_index + max_len]
