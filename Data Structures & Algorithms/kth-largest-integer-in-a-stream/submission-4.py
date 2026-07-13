import heapq as hq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k

        for num in nums:
            if len(self.heap) == k:
                hq.heappushpop(self.heap, num)
            else:
                hq.heappush(self.heap, num)        

    def add(self, val: int) -> int:
        if len(self.heap) == self.k:
            hq.heappushpop(self.heap, val)
        else:
            hq.heappush(self.heap, val) 
        
        return self.heap[0]
    
