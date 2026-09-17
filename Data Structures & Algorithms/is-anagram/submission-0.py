class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq_s = {}
        for char in s:        
            if char not in freq_s:
                freq_s[char] = 1
            else: 
                freq_s[char] = freq_s[char]+ 1

        print(freq_s)
        for char in t:
            if char in freq_s:
                freq_s[char] -= 1
                
                if freq_s[char] == 0:
                    del freq_s[char]

        print(freq_s)
        if not freq_s:
            return True
        
        return False