class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse = True)
        n = len(nums)
        i = 0
        while i < n and nums[i] > i:
            i += 1
        return -1 if i < len(nums) and nums[i] == i else i