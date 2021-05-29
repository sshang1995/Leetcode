class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # sum(longest subarray) = sum(nums) - x
        total = sum(nums)
        target = total - x
        n = len(nums)
        sums = j = 0
        res = -1
        for i in range(n):
            sums += nums[i]
            while sums > target and j <= i:
                sums -= nums[j]
                j += 1
            if sums == target:
                res = max(res, i-j+1) 
        return n-res if res != -1 else -1

# TC: O(N)
# SC: O(1)
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # sum(longest subarray) = sum(nums) - x
        curr = sum(nums)
        n = len(nums)
        j = 0
        res = inf
        for i in range(n):
            curr -= nums[i]
            while curr < x and j <= i:
                curr += nums[j]
                j += 1
            if curr == x:
                res = min(res, j+ n-i-1)
                
        return res if res != inf else -1
                
            
# directly two pointer.
# TC: O(N)
# SC: O(1)