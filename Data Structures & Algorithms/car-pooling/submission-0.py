class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        stops = []

        for ppl, pickup, dropoff in trips:
            stops.append([pickup, ppl])
            stops.append([dropoff, -ppl])
        
        stops.sort()
        personTally = 0

        for stop, ppl in stops:
            personTally += ppl

            if personTally > capacity:
                return False


        return True