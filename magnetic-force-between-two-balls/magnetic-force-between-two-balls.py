class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # binary search
        n = len(position)
        position = sorted(position)
        
        # count(d) function to find max d
        def count(d):
            res = 1 # start from 1 ball
            curr = position[0]
            for i in range(1, n):
                if position[i] - curr >= d:
                    res += 1
                    curr = position[i]
            return res
        l = 0
        r = position[-1] - position[0]
        while l < r:
            mid = r - (r - l) //2
            if count(mid) >= m:
                l = mid
            else:
                r = mid -1
        return l
            