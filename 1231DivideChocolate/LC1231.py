class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        if len(sweetness) == K+1:
            return min(sweetness)
        l = 1
        r = sum(sweetness) // (K+1)
        while l < r:
            mid = (l + r +1)//2
            count = sums = 0
            for i in sweetness:
                sums += i
                if sums >= mid:
                    count += 1
                    sums = 0
                
            if count >= K+1:
                l = mid 
            else:
                r = mid-1

        return l