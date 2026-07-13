class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        maxElements = []
        left = 0
        
        for right, val in enumerate(nums):
            while dq and dq[-1] < val:
                dq.pop()
            dq.append(val)

            if right >= k - 1:
                maxElements.append(dq[0])
                
                if nums[left] == dq[0]: 
                    dq.popleft()    
                left += 1
        
        return maxElements
