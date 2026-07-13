'''
- we can say that we essentially are making two subsets at any target value:
    - Let S1 be, the subset holding the sum of numbers we assinged "+" to
    - Let S2 be, the subset holding the sum of numbers we assigned "-" to

- We can say:
    - S1 - S2 = target
    - S1 + S2 = totalSum 
- Using that we can say that:
    - S1 = (target + total_sum) / 2

So now we have to find how many S1 subsets we can make at each number upto target

0/1 knapsack
'''

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        totalSum = sum(nums)

        if (
            abs(target) > totalSum or 
            (totalSum + target) % 2 != 0
        ):
            return 0
        
        subsetSum = (totalSum + target) // 2 # Capacity
        dp = [0] * (subsetSum + 1)
        dp[0] = 1 # One way to make nothing by not picking

        for n in nums:
           for capacity in range(subsetSum, n - 1, -1):
            # The ways to make sum 'capacity' is the current ways, 
            # PLUS the ways we could make 'capacity - num' before adding this number.
            dp[capacity] = dp[capacity] + dp[capacity - n]

        return dp[subsetSum]
