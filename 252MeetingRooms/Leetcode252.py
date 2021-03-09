# brute force
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        for i in range(len(intervals)):
            for j in range(i+1,len(intervals)):
                #check overlap, check start time between another interval or not
                if (intervals[i][0]>=intervals[j][0] and intervals[i][0]<intervals[j][1]) or (intervals[j][0]>=intervals[i][0] and intervals[j][0] <intervals[i][1]):
                    return False
        return True
#another way to check overlap:
#minEnd > maxStart
def overlap(interval1, interval2):
    return min(interval1[1], interval2[1]) > max(interval1[0], interval2[0])


#sorting: very fast
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(len(intervals)-1):
            if intervals[i][1]> intervals[i+1][0]:
                return False
        return True

# optimize, save memory like Meeting room 2
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        st = []
        en = []
        for interval in intervals:
            st.append(interval[0])
            en.append(interval[1])
        st = sorted(st)
        en = sorted(en)
        i, j =0,0
        room =0
        while i < len(intervals):
            if st[i] >= en[j]:
                room -= 1
                j+=1

            i+=1
            room+=1
            if room >1:
                return False
        return True