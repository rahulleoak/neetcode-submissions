class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        heap = [[-cnt, ch] for ch, cnt in freq.items()]
        heapq.heapify(heap)

        curr = None
        res = []

        while heap or curr:
            if curr and not heap:
                return ''
            
            cnt, ch = heapq.heappop(heap)
            res.append(ch)
            cnt += 1

            if curr:
                heapq.heappush(heap, curr)
                curr = None
            
            if cnt != 0:
                curr = [cnt, ch]

        
        return ''.join(res)

