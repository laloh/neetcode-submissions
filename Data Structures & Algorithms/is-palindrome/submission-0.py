class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s_alpha = ""
        for char in s:
            if char.isalnum():
                s_alpha += char.lower()

        start, end = 0, len(s_alpha) - 1
        #          v
        # WasitacaroracatIsaw
        #          ^  
        while start < end:
            if s_alpha[start] != s_alpha[end]:
                return False
            start += 1
            end -= 1
        
        return True

        