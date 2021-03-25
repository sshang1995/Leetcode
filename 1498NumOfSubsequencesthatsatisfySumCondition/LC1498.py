class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums = sorted(nums)
        total = 2 ** n -1
        mod = 10**9 +7
        if nums[-1]*2 <= target:
            return total % mod
        for i in range(n):
            # deduct unsatisfied subsequence,if nums[i] is too big.
            if nums[i] *2 > target:
                total = total - 2 ** (n-i) +1
                return total % mod
            # deduct subsequnce, when min+ max is too big
            for j in range(i+1, n):
                
                if nums[i] + nums[j] > target:
                    total -= 2**(j-i-1)  
                    
        return total % mod   
    # TC: O(N^2)
    # SC: O(1)

# optimized Two sum 
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        A = sorted(nums)
        l, r = 0, len(A) - 1
        res = 0
        mod = 10**9 + 7
        while l <= r:
            if A[l] + A[r] > target:
                r -= 1
            else:
                res += pow(2, r - l, mod)
                l += 1
        return res % mod

# TC: O(NLogN)
# SC: O(1)
          