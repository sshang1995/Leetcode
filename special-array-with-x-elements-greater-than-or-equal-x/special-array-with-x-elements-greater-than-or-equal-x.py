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