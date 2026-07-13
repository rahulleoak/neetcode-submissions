"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
import copy
class Solution:
    def __init__(self):
        self.copyMap = {}
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None 
            
        q = deque()
        self.copyMap[node] = Node(node.val)
        q.append(node)

        while q:
            curr = q.popleft()
            
            for nei in curr.neighbors:
                if nei not in self.copyMap:
                    self.copyMap[nei] = Node(nei.val)
                    q.append(nei)
                self.copyMap[curr].neighbors.append(self.copyMap[nei])
        

        return self.copyMap[node]
                
