class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store[key]
        
        left, right = 0, len(values)-1
        while left <= right:
            mid = (left + right) // 2
            val, ts = values[mid]

            if ts <= timestamp:
                res = val
                left = mid + 1
            else:
                right = mid - 1
        
        return res
