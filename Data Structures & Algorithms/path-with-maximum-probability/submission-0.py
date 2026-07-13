class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adjList = defaultdict(list)
        
        for (src, dst), prob in zip(edges, succProb):
            adjList[src].append((dst, prob))
            adjList[dst].append((src, prob))

        maxHeap =[(-1, start_node)]
        visited = set()

        while maxHeap:
            prob, node = heapq.heappop(maxHeap)
            prob *= -1
            
            visited.add(node)

            if node == end_node:
                return prob
            
            for nei, neiProb in adjList[node]:
                if nei not in visited:
                    heapq.heappush(maxHeap, (-(prob * neiProb), nei))
        
        return 0.0

