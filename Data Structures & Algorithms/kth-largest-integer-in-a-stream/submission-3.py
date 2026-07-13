class MinHeap:
    def __init__(self):
        self.heap = [None]
    
    def push(self, val:int):
        self.heap.append(val)
        idx = len(self.heap) - 1
        self._siftUp(idx)
    
    def pop(self):
        heapLen = len(self.heap)

        if heapLen == 1:
            return None
        elif heapLen == 2:
            return self.heap.pop()
        
        rootVal = self.heap[1]
        self.heap[1] = self.heap.pop()
        idx = 1
        self._siftDown(idx)

        return rootVal
    
    def peek(self):
        return self.heap[1] if len(self.heap) > 1 else None

    def size(self):
        return len(self.heap) - 1

    def _siftUp(self, idx):
        parent = idx // 2

        while (
                idx > 1 and
                self.heap[idx] < self.heap[parent]
        ):
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            idx = parent
            parent = idx // 2
    
    def _siftDown(self, idx):
        
        heapLen = len(self.heap)

        while 2 * idx < heapLen:
            left, right = 2 * idx, 2*idx + 1
            smallest = left
            
            if (
                right < heapLen and
                self.heap[right] < self.heap[left]
            ):
                smallest = right
            
            if self.heap[idx] > self.heap[smallest]:
                self.heap[idx] , self.heap[smallest] = self.heap[smallest], self.heap[idx]
                idx = smallest
            
            else:
                break        

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.stream = MinHeap()        
        

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if self.stream.size() < self.k:
            self.stream.push(val)
        
        elif val > self.stream.peek():
            self.stream.pop()
            self.stream.push(val)
        
        return self.stream.peek()
            
        
