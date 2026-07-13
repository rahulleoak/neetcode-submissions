'''
S: 
    Let dp[i] be the min cost to cover all required travel from day 1 to day i

R:
For any day 'd' in range of 1 to (including) 365
    - if d IS NOT a travel day:
        dp[d] = dp[d-1], since cost is same as the day before since no pass is needed
    - if d IS a travel day:
        we must be covered by a pass to reach day 'd', we look at the min of..
            1. 1-day pass bought the day b4: dp[d-1] + cost[0]
            2. 7-day pass bought a week before: dp[d-7] + cost[1]
            3. 30-day pass bought a month before: dp[d-30] + cost[2]
        dp[d] = min(1day, 7day, 30day)

T:
    increasing order of days

B:
    dp[0] = 0, cost of travelling 0 days is 0 dollars
    For d > 0, we take the max(0, d-passLength)

O:
    dp[lastDay]

T:
    O(365) or O(lastDay)
'''
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        '''
        OPTIMIZATION: 
        - Can just hold 30 days + day 0, since we only at most look back 30 days
        - Use a circular array (day % 31)
        '''
        n = len(days)
        lastDay = days[-1]
        
        # dp[i] is the minimum cost to cover all required travel days up to day 'i'.
        dp = [0] * 31 # 30 days including day 0

        i = 0
        for day in range(1, lastDay+1):
            if i == n:
                return dp[lastDay % 31]
            
            if day == days[i]:
                # A pass bought a day ago to reach today + the cost of a day before
                pass1 = costs[0] + dp[(day-1) % 31]
                # A pass bought 7 days ago to reach today + the cost of a week before
                pass7 = costs[1] + dp[max(0, day-7) % 31]
                # A pass bought 30 days ago to reach today + the cost of a month before
                pass30 = costs[2] + dp[max(0, day-30) % 31]

                dp[day % 31] = min(pass1, pass7, pass30)

                i += 1
            else:
                # For non travel days, cost is the same as previous
                dp[day % 31] = dp[(day-1) % 31]
            
        return dp[lastDay % 31]


'''
days=[1,4,6,7,8,20]
costs=[2,7,15]

day  [0, 1, 4, 6, 7, 8, 20]
dp = [0, 2, 7, 6, 7, 9, 11]

day1:
    1 = 2 + 0   min
    7 = 7 + 0
    30 = 15 + 0

day 2-3: dp[2:3] = [2,2]

day 4:
    min(2+2, 7+0, 15+0)

day 5:  dp[5] = 4

day 6:
    min(2+4, 7+0, 15+0)

day 7:
    min(2+6, 7+0, 15+0)

day 8:
    min(2+7, 7+2, 15+0)

day 9-19: dp[9:19] = [9,9,9,...,9]

day 20:
    min(2+9, 7+9, 15+0)
'''