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