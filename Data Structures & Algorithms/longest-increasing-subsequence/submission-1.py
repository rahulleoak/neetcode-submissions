import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Holds the smallest possible "tails" for incr. subseq of different lengths
        # Represents the LIS
        if not nums:
            return 0

        tails = [nums[0]]

        for idx in range(1, len(nums)):
            num = nums[idx]
            
            # if curr num is greater than the last val in tails, extend the LIS
            if num > tails[-1]:
                tails.append(num)
            
            # Otherwise, find the smallest tail >= nums[i] and replace it nums[i]
            # Doesn't change the len(tails), but optimizes it by replaceing with a better tail
            else:
                idx = bisect.bisect_left(tails, num)
                tails[idx] = num

        return len(tails)


        '''
        TC: O(n2)

        n = len(nums)
        # Let dp[i] be the LIS ending at index i
        dp = [1] * (n)
        
        for nxt in range(n):
            # check all elements before nxt to see if the can form an incr. subseq
            for idx in range(nxt):
                if nums[nxt] > nums[idx]:
                    # dp[nxt] = max of either itself or the max at 'idx' plus 1 (to include "nxt")
                    dp[nxt] = max(dp[idx] + 1, dp[nxt])
        
        return max(dp)
        '''