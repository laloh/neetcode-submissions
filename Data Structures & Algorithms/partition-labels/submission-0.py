class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_ocurrence = {char: i for i, char in enumerate(s)}

        res = []
        start = 0
        max_reach = 0
       
        for i, char in enumerate(s):
            max_reach = max(max_reach, last_ocurrence[char])
    
            if i == max_reach:
                res.append(i - start + 1)
                start = i + 1
        
        return res
