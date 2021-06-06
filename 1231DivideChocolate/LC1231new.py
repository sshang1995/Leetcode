class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        if len(sweetness) == K+1:
            return min(sweetness)
        l = 0
        r = sum(sweetness) //(K + 1) # average sweet
        while l < r:
            mid = (l+r+1) //2
            sums = count = 0
            for i in sweetness:
                sums += i
                if sums >= mid:
                    count += 1
                    sums = 0
            if count >= K+1:
                l = mid 
            else:
                 r = mid -1
        return l
# TC: O(NlogM) N- number of sweetness, M is sum of sweetness
# SC: O(1)
