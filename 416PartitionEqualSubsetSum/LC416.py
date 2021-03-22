class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #brute Force
        def dfs(nums:List[int], n:int, subset_sum: int):
            if subset_sum ==0:
                return True
            if n == 0 or subset_sum < 0:
                return False
            result = (dfs(nums, n-1, subset_sum -nums[n-1])
                     or dfs(nums, n-1, subset_sum))
            return result
        
        total_sum = sum(nums)
        
        if total_sum % 2 != 0:
            return False
        subset_sum = total_sum //2
        n = len(nums)
        
        return dfs(nums, n-1, subset_sum)
    
    #TC: O(2^n) The recursive solution takes the form of a binary tree where there are 2 possibilities for every array element and the maximum depth of the tree could be nn. The time complexity is exponential, hence this approach is exhaustive and results in Time Limit Exceeded (TLE).
    #SC: O(N) store recursion stack, we can't have more than n recursive calls on the call stack at any time.

  # memoization
    class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @lru_cache(maxsize=None) # Least recently used 
       # Dp memoization: computing once and returning the stored value 
        def dfs(nums: Tuple[int], n: int, subset_sum: int):
            if subset_sum == 0:
                return True
            if n == 0 or subset_sum < 0:
                return False
            
            result = (dfs(nums, n -1, subset_sum-nums[n-1]) or dfs(nums, n-1, subset_sum))
          
            return result
        
        
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        subset_sum = total_sum // 2
        n = len(nums)
        
        return dfs(tuple(nums),n-1,subset_sum)

    # TC: O(m * n) Let n be the number of array elements and m be the subSetSum.
    # SC: O(m * n)

    # optmized Dp using 1D array
    class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        if total_sum % 2 != 0:
            return False
        subset_sum = total_sum //2
        
        dp = [False] * (subset_sum + 1)
        dp[0] = True
        for curr in nums:
            for j in range(subset_sum, curr-1, -1):
                dp[j] = dp[j] or dp[j-curr]
                
        return dp[subset_sum]
    
    # TC: O(m * n) m is the subset_sum, n is the number of array elements
    # SC: O(m) 
        