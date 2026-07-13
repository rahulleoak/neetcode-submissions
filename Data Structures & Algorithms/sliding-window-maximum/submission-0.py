class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        dq = deque()
        left = 0

        for right, val in enumerate(nums):

            while dq and dq[0] < left:
                dq.popleft()

            while dq and val > nums[dq[-1]]:
                dq.pop()            
            dq.append(right)


            if (right - left + 1) == k:
                localMax = nums[dq[0]]
                res.append(localMax)
                left += 1
        
        return res
            
                