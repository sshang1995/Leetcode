class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        res = 0
        boxTypes = sorted(boxTypes, key=lambda x:x[1], reverse=True)
        curr_truckSize = truckSize
        for item in boxTypes:
            if item[0] <= curr_truckSize:
                res += item[0] * item[1]
                curr_truckSize -= item[0]
            else:
                if curr_truckSize > 0:
                    res += curr_truckSize * item[1]
                    curr_truckSize -= curr_truckSize
        return res