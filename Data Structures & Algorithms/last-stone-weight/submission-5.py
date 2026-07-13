class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            firstStone = -1 * heapq.heappop(heap)
            secondStone = -1 * heapq.heappop(heap)

        
            if secondStone < firstStone:
                heapq.heappush(heap, -(firstStone-secondStone))
        
        return abs(heap[0]) if heap else 0