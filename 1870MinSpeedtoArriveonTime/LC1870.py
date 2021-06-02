class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)
        if hour < n-1:
            return -1
        lo = 1
        hi = 10**7 +1
        while lo < hi:
            speed = lo + (hi -lo) // 2
            time = 0
            for i in range(n-1):
                time += (dist[i] + speed -1) // speed 
            time += dist[-1] / speed
            if time > hour:
                lo = speed +1
            else:
                hi = speed
        return -1 if lo == 10**7 +1 else lo

# TC: O(NlogK) K is speed searce space,