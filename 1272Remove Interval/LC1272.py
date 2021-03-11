class Solution:
    def removeInterval(self, intervals: List[List[int]], r: List[int]) -> List[List[int]]:
        
        output = []
        for i in intervals:
            # add non-overlap intercal
            if i[1] < r[0] or i[0] > r[1]:
                output.append(i)
            else: #if overlapped
                # exclude overlap part 
                if i[0] < r[0]:
                    output.append([i[0],r[0]])
                if i[1] > r[1]:
                    output.append([r[1],i[1]])
        return output