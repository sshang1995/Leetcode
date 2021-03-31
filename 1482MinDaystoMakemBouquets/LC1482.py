class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        s = 1
        e = max(bloomDay)
        
        while s < e:
            mid = (s + e) //2
            count = nums = 0
            for day in bloomDay:
                if day <= mid:
                    count += 1
                else:
                    count = 0
                if count ==k:
                    nums += 1
                    count = 0
            if nums < m:
                s = mid +1
            else:
                e = mid  
        return s
    