class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        res = 0
        boxTypes = sorted(boxTypes, key=lambda x:x[1], reverse=True)
        for item in boxTypes:
            if item[0] <= truckSize:
                res += item[0] * item[1]
                truckSize -= item[0]
            else:
                if truckSize > 0:
                    res += truckSize * item[1]
                    truckSize = 0 
                    break
        return res