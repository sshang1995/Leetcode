class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = collections.Counter({0:1})
        ans = presum = 0
        for i in nums:
            presum += i
            ans += count[presum-goal]
            count[presum] += 1
        return ans