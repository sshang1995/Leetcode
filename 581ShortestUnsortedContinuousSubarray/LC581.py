class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        res = []
        sorted_nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                res.append(i)
        #print(res)
        return 0 if not res else res[-1] - res[0] + 1
# TC: O(NlogN)
# SC: O(N)