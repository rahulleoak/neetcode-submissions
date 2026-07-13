class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for val in nums:
            if len(minHeap) == k:
                heapq.heappushpop(minHeap, val)
            else:
                heapq.heappush(minHeap, val)
                
            print(minHeap)
        return minHeap[0]