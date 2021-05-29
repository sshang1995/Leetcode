class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sums = res = 0
        maps = {0:-1} # prefix_sum: index
        for i in range(n):
            sums += nums[i]
            if sums not in maps:
                maps[sums] = i
            if sums - k in maps:
                res = max(res, i- maps[sums-k])
        return res