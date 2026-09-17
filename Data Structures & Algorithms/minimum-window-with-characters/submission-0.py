class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if not s or not t:
            return ""

        target_count = Counter(t)
        required = len(target_count)
        formed = 0
        left, right = 0, 0
        window_counts = {}
        min_length = float("inf")
        result = (float("inf"), None, None)

        for right in range(len(s)):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1
            if char in target_count and window_counts[char] == target_count[char]:
                formed += 1
            while left <= right and formed == required:
                char = s[left]
                if right - left < min_length + 1:
                    min_length = right - left + 1
                    result = (min_length, left, right)
                window_counts[char] -= 1
                if char in target_count and window_counts[char] < target_count[char]:
                    formed -= 1
            
                left += 1
        return "" if result[0] == float("inf") else s[result[1]:result[2]+1]
