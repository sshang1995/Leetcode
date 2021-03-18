class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
       # get earliest slot
        slots1.sort(key = lambda x: x[0])
        slots2.sort(key = lambda x: x[0])
        i = j = 0
        while i < len(slots1) and j < len(slots2):
            # find intersection
            if slots1[i][0]<= slots2[j][0] and slots2[j][0] <= slots1[i][1]:
                end = min(slots1[i][1], slots2[j][1])
                if end - slots2[j][0] >= duration:
                    return [slots2[j][0],slots2[j][0]+duration]
                if slots1[i][1] > slots2[j][1]:
                    j +=1
                else:
                    i+=1
                
            elif slots2[j][0] <=slots1[i][0] and slots1[i][0] <= slots2[j][1]:
                end = min(slots1[i][1], slots2[j][1])
                if end - slots1[i][0] >= duration:
                    return [slots1[i][0], slots1[i][0] + duration]
                if slots1[i][1] < slots2[j][1]:
                    i+=1
                else:
                    j+=1
            
            elif slots1[i][1] < slots2[j][0]:
                i += 1
            elif slots1[i][0] > slots2[j][1]:
                j += 1
        return []