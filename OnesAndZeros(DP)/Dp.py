
# iterative
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        def count(s):
            return sum(1 for c in s if c == '0'), sum(1 for c in s if c == '1')
        
        for zeros, ones in [count(s) for s in strs]:
            for z in range(m, -1, -1):
                for o in range(n, -1, -1):
                    if zeros <= z and ones <= o:
                        dp[z][o] = max(1 + dp[z-zeros][o-ones], dp[z][o])
        # 1 + dp[z-zeros][o-ones], CountAddingStr
        #dp[z][o], CountskippingStr
        return dp[m][n]

#T : O(MNK) K is length of str
#S: O(MN)

#recursive
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        arr = [[s.count('0'), s.count('1')] for s in strs]
        
        @lru_cache(None)
        def dp(i, m, n):
            if i == len(strs):
                return 0
            
            ans = dp(i+1, m, n) # Skip strs[i]
            if m >= arr[i][0] and n >= arr[i][1]:
                ans = max(ans, dp(i+1, m-arr[i][0], n-arr[i][1]) + 1) # Pick strs[i]
            return ans
        
        return dp(0, m, n)

#T: O(MNK)
#S: O(MNK)