class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegreeDelta = defaultdict(int)
    
        for src, dst in trust:
            indegreeDelta[src] -= 1
            indegreeDelta[dst] += 1
        
        for key in indegreeDelta:
            if indegreeDelta[key] == n-1:
                return key
        return -1

        