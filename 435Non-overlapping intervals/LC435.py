class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <=1:
                    return 0
        # Greedy: earliest end time could have maximum non-overlapping intervals (or minmum number to remove), the earliest end time has biggest capacity to hold more intervals.
        intervals.sort(key = lambda x: x[1])
        end = float('-inf')
        count = 0
        for s, e in intervals:
            if s >= end:
                end = e
            else:
                count +=1 
        return count
            