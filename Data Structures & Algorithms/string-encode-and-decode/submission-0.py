class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            word_length = len(word)
            res += f"{word_length}#{word}"

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            for j in range(i, len(s)):
                if s[j] == "#":
                    length = int(s[i:j])
                    res.append(s[j+1: j+1 + length])
                    break
            
            i = j + 1 + length
        
        return res