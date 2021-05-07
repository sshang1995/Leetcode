class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        # Top Down
        n = len(arr)
        res = [0] * n
        
        def dp(i):
            if res[i]:
                return res[i]
            res[i] = 1
            for di in [-1, 1]:
                for j in range(i+di, i + d*di+di, di):
                    if not (0 <= j < n and arr[j] < arr[i]):
                        break
                    res[i] = max(res[i], dp(j) +1)
            return res[i]
        return max(map(dp, range(n)))
                        

# for each step arr[i], check arr[j] on the left and right, until it meet the end or bigger step
#TC: O(ND)
# SC: O(N)

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        # bottom up
        n = len(arr)
        dp = [1] *n
        for a, i in sorted([a, i] for i, a in enumerate(arr)):
            for di in [-1,1]:
                for j in range(i + di, i + d * di + di, di):
                    if not (0<=j<n and arr[j] < arr[i]):
                        break
                    dp[i] = max(dp[i], dp[j] +1)
        return max(dp)
#TC: O(NlogN+ ND)
#SC: O(N)