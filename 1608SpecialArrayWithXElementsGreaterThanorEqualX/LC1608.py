class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for i in range(len(nums)+1):
            count = 0
            for index, j in enumerate(nums):
                if j >= i:
                    count += 1
                if count > i:
                    break
                if index == len(nums) - 1 and count == i:
                    return i
        return -1

# TC：O(N^2)
# SC：O(1)

# sort reverse
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse = True)
        i = 0
        while i < len(nums) and nums[i] > i:
            i += 1
        return -1 if i < len(nums) and nums[i] == i else i
# TC: O(NlogN)
# SC: O(1)

# binary search
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse = True)
        left = 0
        right = len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if mid < nums[mid]:
                left = mid +1 
            else:
                right = mid
        return -1 if left < len(nums) and nums[left] == left else left

# TC: O(NlogN)
# SC: O(1)
