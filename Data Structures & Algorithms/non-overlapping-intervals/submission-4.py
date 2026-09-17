class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        if len(intervals) == 1:
            return 0

        intervals.sort(key=lambda x: x[0])
        print(intervals)

        count = 0
        last_end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start < last_end:
                count += 1
                last_end = min(end, last_end)
            else:
                last_end = end

        return count 