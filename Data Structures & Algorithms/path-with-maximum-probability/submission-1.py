class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adjList = defaultdict(list)
        
        for (src, dst), prob in zip(edges, succProb):
            adjList[src].append((dst, prob))
            adjList[dst].append((src, prob))

        maxHeap =[(-1, start_node)]
        maxProb = {}
        maxProb[start_node] = 1

        while maxHeap:
            prob, node = heapq.heappop(maxHeap)
            prob *= -1
            
            if maxProb.get(node, 0) > prob:
                continue

            if node == end_node:
                return prob
            
            for nei, neiProb in adjList[node]:
                newProb = prob * neiProb
                if newProb > maxProb.get(nei, 0):
                    maxProb[nei] = newProb
                    heapq.heappush(maxHeap, (-newProb, nei))
        
        return 0.0