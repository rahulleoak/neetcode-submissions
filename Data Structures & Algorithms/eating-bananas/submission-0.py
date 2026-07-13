class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def valid (rate):
            elapsed = 0
            for p in piles:
                elapsed +=  math.ceil( p / rate)

            return elapsed <= h
        
        lo, hi = 1, max(piles)

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if valid(mid):
                hi = mid - 1
            else:
                lo = mid + 1

        return lo