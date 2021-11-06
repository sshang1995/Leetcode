class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums)
        elif target <= nums[0]:
            return 0
        
        left, right = 0, len(nums) - 1
        while left < right:
            p = left + (right - left)//2
            if nums[p] > target:
                right = p 
            elif nums[p] == target:
                return p
            else:
                left = p + 1
        return left
        