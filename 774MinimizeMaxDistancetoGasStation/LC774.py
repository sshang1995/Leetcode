class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        
        l = 0
        r = 10 ** 8 
        while r- l > 1e-6:
            mid = (l + r) / 2
            count = 0
            for i in range(1, len(stations)):
                count += (stations[i]-stations[i-1]) //mid
            if count <= k:
                r = mid
            else:
                l = mid
        return l