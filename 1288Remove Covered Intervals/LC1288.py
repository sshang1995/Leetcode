# my version:
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x: x[0])
        prev = intervals[0]
        count = 0
        for i in range(1, len(intervals)):
            # current interval is covered by previous one
            if intervals[i][0] >= prev[0] and intervals[i][1] <= prev[1]:
                count += 1
            # current interval cover previous one
            elif intervals[i][0]<=prev[0] and intervals[i][1]>=prev[1]:
                count +=1
                prev = intervals[i]
            else:
                prev = intervals[i]
        return len(intervals) - count
 
# optimized version           
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x: (x[0], -x[1]))
        prev_end = 0
        count = 0
        for _, end in intervals:
            # count uncovered interval
            if end > prev_end:
                count += 1
                prev_end = end 
        return count

