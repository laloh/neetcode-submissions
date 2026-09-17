class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        count = Counter(hand)
        sorted_keys = sorted(count.keys())
        groups = []

        for card in sorted_keys:
            if count[card] > 0:
                start_count = count[card]
                group = []
                for i in range(card, card+groupSize):
                    if count[i] < start_count:
                        return False
                    count[i] -= start_count
                    group.append(i)
                groups.append(group)
        print(groups)
        return True
            
