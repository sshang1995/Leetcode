class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if not nums:
            return False
        total_sum = sum(nums)
        if total_sum % 4 !=0:
            return False
        side = total_sum // 4
        
        nums.sort(reverse=True)
        sums = [0 for _ in range(4)]

        def dfs(index):
            if index == len(nums):
                return sums[0] == sums[1]==sums[2]==sums[3]==side
            # 4 side.
            for i in range(4):
                if sums[i] + nums[index] <= side:
                    sums[i] += nums[index]
                    # recurse
                    if dfs(index +1):
                        return True
                    # revert the effects of recursion because we no longer need them for other recursions
                    sums[i] -= nums[index]
            return False
        return dfs(0)
# TC: O(4^N)
# SC: O(N) The deepesy recursive call here would be of size N.

# optimized, memoization
