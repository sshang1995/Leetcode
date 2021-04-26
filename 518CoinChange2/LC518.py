class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        def dfs(amount, coins, idx, memo):
            if (amount, idx) in memo:
                #print(f"{(amount,idx)},{memo[(amount, idx)]}")
                return memo[(amount, idx)]
            if amount == 0:
                return 1
            cnt = 0
            for i in range(idx,len(coins)): 
                if amount - coins[i] < 0:
                    break
                cnt += dfs(amount- coins[i], coins, i, memo) 
            
            memo[(amount, idx)] = cnt
            return cnt
        if not coins:
            if amount == 0:
                return 1
            return 0
        coins = sorted(coins)
        return dfs(amount,coins, 0, {})
                    
# dfs: TC: O(V+E) +O(NLogN) V is number of node, E is number of edges
     # SC: O(N)

# dp
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #define amount from 0 to amount 
        dp = [0]* (amount +1)
        # base case No coins or amount = 0, there is only one combination, take zero coins.
        dp[0] = 1
        for coin in coins:
            for x in range(coin, amount+1):
                dp[x] += dp[x-coin]
        return dp[amount]
# TC: O(N * amount) N is length of coins array
#SC: O(amount) dp array.