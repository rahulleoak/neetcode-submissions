class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def helper(value):
            if value == 0:
                return 0
            
            if value in memo:
                return memo[value]

            coinCombo = float('inf')
            for coin in coins:
                if value - coin >= 0:
                    coinCombo = min(coinCombo, helper(value - coin) + 1)
            
            memo[value] = coinCombo
            return memo[value]
        
        minCoinCombo = helper(amount)
        return -1 if minCoinCombo == float('inf') else minCoinCombo