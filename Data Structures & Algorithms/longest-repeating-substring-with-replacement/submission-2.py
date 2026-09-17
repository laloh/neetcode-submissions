class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        max_freq = 0
        freq = {}
        start = 0
        max_length = 0

        for end in range(len(s)):

            char = s[end]

            if char not in freq:
                freq[char] = 0
            freq[char] += 1

            max_freq = max(max_freq, freq[char])

            if (end - start + 1) - max_freq > k:
                freq[s[start]] -= 1
                start += 1

            
            max_length = max(max_length, end - start + 1)
        
        return max_length