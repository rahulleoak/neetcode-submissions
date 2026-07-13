class Solution:
    def rob(self, nums: List[int]) -> int:
        # p -> q -> c -> n
        #      p -> q -> c ->

        p = q = 0

        for num in nums:
            p , q = q, max(num + p, q) 
        
        return q