class Solution:
    def numDecodings(self, s: str) -> int:
        
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        dp = [0] * (n + 1)
        
        # Base cases  
        dp[0] = 1 # An empty string has 1 valid empty decoding
        dp[1] = 1 # The first character (since it's not 0) has 1 decoding

        for i in range(2, n + 1):
            # Check sing-digit decode (the character at index i - 1)
            one_digit = s[i - 1]
            print(f"One digit: {s[i - 1]} ", one_digit)
            if one_digit != '0':
                dp[i] += dp[i - 1]
            
            # Check two-digit decode (the character at indices i - 2 and i - 1) 
            two_digit = int(s[i - 2 : i])
            print(f"Two digit: {s[i - 2: i]} ", two_digit)
            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]
        
        return dp[n]

