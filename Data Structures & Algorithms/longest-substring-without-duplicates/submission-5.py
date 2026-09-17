class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_length = 0
        left = 0
        freq = {}
        for right in range(len(s)):

            char = s[right]
            if char in freq and freq[char] >= left:
                left = freq[char] + 1
            
            freq[char] = right
            max_length = max(max_length, right - left + 1)

        return max_length