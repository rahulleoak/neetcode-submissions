class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0: return 0
        
        # Max profit on day 'i' if we end the day holding a stock.
        hold = [0] * n
        hold[0] = -prices[0] # We bought on day 0
        
        # Max profit on day 'i' if we end the day having just sold our stock.
        sell = [0] * n
        sell[0] = 0 # Impossible to sell on day 0
        
        # Max profit on day 'i' if we end the day with empty hands (rest/cooldown).
        rest = [0] * n
        rest[0] = 0 # We did nothing on day 0

        for idx in range(1,n):
            # 1. HELD STATE: 
            #   We either kept holding from yesterday (OR)
            #   We bought today (spending money from yesterday's 'rest' state)
            hold[idx] = max(hold[idx-1], rest[idx-1] - prices[idx])

            # 2. SOLD STATE: 
            #   We MUST have sold the stock we were holding yesterday
            sell[idx] = hold[idx-1] + prices[idx]

            # 3. REST STATE: 
            #   We either kept resting from yesterday (OR)
            #   Our cooldown from yesterday's 'sold' state just finished
            rest[idx] = max(rest[idx-1], sell[idx-1])


        return max(rest[n-1], sell[n-1])
