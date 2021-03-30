import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(mid):
            hours = 0
            for p in piles:
                hours += math.ceil(p/mid)
            return hours <= h
        
        start = 1
        end = max(piles)
        #Binary search
        while start < end:
            # or start <= end
            mid = (start + end)//2
            if check(mid):
                end = mid
                # or end = mid -1
            else:
                start = mid +1
        return start