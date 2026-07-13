import heapq as hq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        freq = [(-a,"a"), (-b, "b"), (-c,"c")]
        heap = []
        for cnt, ch in freq:
            if cnt != 0:
                hq.heappush(heap,[cnt, ch])
        
        
        res = []
        while heap:
            cnt, ch = hq.heappop(heap)

            if len(res) > 1 and res[-1] == res[-2] == ch:
                if not heap:
                    break
                
                nextCnt, nextCh = hq.heappop(heap)
                res.append(nextCh)
                nextCnt += 1

                if nextCnt != 0:
                    hq.heappush(heap, [nextCnt, nextCh])
                hq.heappush(heap, [cnt, ch])
            
            else:
                res.append(ch)
                cnt += 1
                if cnt != 0:
                    hq.heappush(heap, [cnt,ch])
        
        return ''.join(res)





