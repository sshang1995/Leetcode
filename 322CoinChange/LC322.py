class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount <= 0: 
            return 0
        def dfs(coins, remain, count):
            if remain < 0:
                return -1
            if remain == 0:
                return 0
            if count[remain -1] != 0:
                return count[remain -1]
            min = float('inf')
            for coin in coins:
                res = dfs(coins, remain - coin, count)
                if res >=0 and res < min:
                    # plus one coin each time
                    min = res + 1
            if min == float('inf'):
                count[remain -1] = -1
            else:
                count[remain -1] = min
            return count[remain - 1]
        count = [0 for _ in range(amount)]
        return dfs(coins, amount, count)
# DP - Top Down
#TC: O(S*N) S is amount, N is coins
#SC: O(S) we use S space for memoization table.

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for x in range(coin, amount +1):
                dp[x] = min(dp[x], dp[x-coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

# Dp - Bottom up
#TC: O(S*N)
#SC: O(S)
