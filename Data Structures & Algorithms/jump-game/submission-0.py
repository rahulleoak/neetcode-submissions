class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0

        for idx, jump in enumerate(nums):
            if idx > farthest:
                return False
            
            farthest = max(farthest, idx + jump)

            if farthest >= len(nums)-1:
                return True
        
