class TimeMap:

    def __init__(self):
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key in self.keyStore:
            values = self.keyStore[key]
        else:
            values = []

        lo, hi = 0, len(values) - 1
        res = ""
        while lo <= hi:
            mid = lo + (hi-lo) // 2
            
            if timestamp >= values[mid][1]:
                lo = mid + 1
                res = values[mid][0]
            else:
                hi = mid - 1
        
        return res


