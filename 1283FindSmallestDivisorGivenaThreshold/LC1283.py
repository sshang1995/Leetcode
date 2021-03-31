import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        r = max(nums)
        l = 1
        while l < r:
            mid = (l + r) //2 
            sums = 0
            for i in nums:
                sums += math.ceil(i/mid) 
            if sums > threshold:
                l = mid + 1
            else:
                r = mid 
        return l
                