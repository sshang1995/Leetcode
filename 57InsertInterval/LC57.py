class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda x: x[0])
        res = []
        for i in intervals:
            if not res or res[-1][1] < i[0]:
                res.append(i)
            else:
                res[-1][1] = max(res[-1][1], i[1])
        return res
    
    # TC: O(NlogN)



# greedy: TC: O(N)
    class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        index = 0
        n = len(intervals)
        # add inerval have smaller start than newInterval start
        while index < n and newInterval[0] > intervals[index][0]:
            output.append(intervals[index])
            index += 1
        # merge or append new interval
        if not output or output[-1][1] < newInterval[0]:
            output.append(newInterval)
        else:
            output[-1][1] = max(newInterval[1],output[-1][1])
        
        # merge or append left interval 
        while index < n:
            
            if output[-1][1] < intervals[index][0]:
                output.append(intervals[index])
            else:
                output[-1][1] = max(intervals[index][1], output[-1][1])
                
            index +=1
        return output