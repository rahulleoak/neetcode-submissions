class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0 
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        

        startingPoint = 0
        while True:
            slow = nums[slow]
            startingPoint = nums[startingPoint]

            if startingPoint == slow:
                return slow
        