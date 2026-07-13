class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        distance and time are each "proportional"
        therefore: at what time will  the car reach the target position?
            time = distance / speed = (target - position) / speed
        can use a mono stack
        '''
        coord = sorted(zip(position, speed), key=lambda x:x[0], reverse=True)
        stack = []

        for p, s in coord:
            timeToTarget = (target - p) / s

            if not stack or stack[-1] < timeToTarget:
                stack.append(timeToTarget)
        
        return len(stack)

