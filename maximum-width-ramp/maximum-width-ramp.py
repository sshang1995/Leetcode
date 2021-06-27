class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        res = 0
        for i, val in enumerate(nums):
            if not stack or nums[stack[-1]] > val:
                stack.append(i)
        print(stack)
        for i in range(len(nums))[::-1]:
            while stack and nums[i] >= nums[stack[-1]]:
                res = max(res, i - stack.pop())
        return res
                        
