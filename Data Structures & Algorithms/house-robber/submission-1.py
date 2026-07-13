class Solution:
    def rob(self, nums: List[int]) -> int:
        check1,  check2 = 0, 0
        for num in nums:
            check1 , check2 = max(num + check2, check1), check1
        
        return check1