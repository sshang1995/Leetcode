class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        # earliest end balloon decide the maxium number of balloons can be bursted by current arrow.
        points.sort(key = lambda x: x[1])
        prev_end = points[0][1]
        count = 1
        for i in range(1, len(points)):
            # always tracking of current balloon end, ignore all the balloons which start before current end.
            if points[i][0] > prev_end:
                count += 1
                prev_end = points[i][1]
           
        return count