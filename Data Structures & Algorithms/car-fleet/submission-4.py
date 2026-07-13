class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = list(zip(position,speed))
        car.sort(key = lambda x:x[0], reverse = True)

        prevTime = 0
        fleet = 0

        for p, s in car:
            time = (target - p)/ s

            if time > prevTime:
                fleet += 1
                prevTime = time
            
        return fleet
