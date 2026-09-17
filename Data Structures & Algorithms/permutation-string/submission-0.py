class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        freq_s1 = {}
        for c in s1:
            if c not in freq_s1:
                freq_s1[c] = 0
            freq_s1[c] += 1
        
        start = 0
        matches = 0
        for end in range(len(s2)):
            char = s2[end]
            if char in freq_s1:
                freq_s1[char] -= 1
                if freq_s1[char] == 0:
                    matches += 1
            
            # keep the window length
            if (end - start + 1) > len(s1):
                start_char = s2[start]
                if start_char in freq_s1:
                    if freq_s1[start_char] == 0:
                        matches -= 1
                    freq_s1[start_char] += 1   
                start += 1
        
            if matches == len(freq_s1):
                print(matches, len(freq_s1))

                return True
            
        return False