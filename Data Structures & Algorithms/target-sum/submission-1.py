class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1


        for num in nums:
            newDP = defaultdict(int)

            for currTotal, ways in dp.items():
                newDP[currTotal + num] += ways
                newDP[currTotal - num] += ways

            dp = newDP
        
        return dp[target]


