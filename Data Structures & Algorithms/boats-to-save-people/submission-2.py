class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        maxSize = max(people)
        count = [0] * (maxSize + 1)

        for p in people:
            count[p] += 1
        # [0,1,2,2]

        idx, countPtr, = 0, 1
        while idx < len(people):
            while count[countPtr] == 0:
                countPtr += 1
            
            people[idx] = countPtr
            idx += 1

            count[countPtr] -= 1

        # people = [1, 2, 2, 3, 3]
        l, r = 0, len(people) - 1
        boats = 0
        
        while l <= r:
            capacity = limit - people[r]
            r -= 1

            if l <= r and capacity - people[l] >= 0:
                l += 1

            boats += 1
        
        return boats
