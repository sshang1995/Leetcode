class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # longest subarray = sum(nums) - x
        total = sum(nums)
        target = total - x
        sums = j = 0
        res = -1
        for i in range(len(nums)):
            sums += nums[i]
            while sums > target and j <=i :
                sums -= nums[j]
                j += 1
            if sums == target:
                res = max(res, i-j+1) 
        return len(nums)-res if res != -1 else -1
                
            
            