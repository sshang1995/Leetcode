class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        if total < p:
            return -1
        if total % p == 0:
            return 0
        res = float(inf)
        for i in range(len(nums)):
            sums = nums[i]
            if (total - sums) % p == 0:
                return 1
            for j in range(i+1, len(nums)):
                if sums + nums[j] < total and (total - sums - nums[j]) % p == 0:   
                    res = min(res, j-i+1)
                    break
                elif  (total - sums - nums[j]) < p or sums + nums[j] == total:
                    break
                else:
                    sums += nums[j]
                
        return res if res < float(inf) else -1
# TLE
# TC: O(N^2)
# SC: O(1)

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        mod = sum(nums) % p 
        # prefix_sum: index 
        dp = {0:-1}
        curr_mod = 0
        res = n = len(nums)
        for i, v in enumerate(nums):
            curr_mod = (curr_mod + v) % p
            dp[curr_mod] = i
            if (curr_mod - mod) % p in dp:
                res = min(res, i - dp[(curr_mod - mod) % p])
        return res if res < n else -1

# TC:O(N)
# SC: O(N)