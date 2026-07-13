class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjList = {i : [] for i in range(numCourses)}
        indegree = [0] * numCourses
        preReq = [set() for i in range(numCourses)]

        for src, dst in prerequisites:
            adjList[src].append(dst)
            indegree[dst] += 1
        
        q = deque([i for i in range(numCourses) if indegree[i] == 0])

        while q:
            node = q.popleft()

            for nei in adjList[node]:
                preReq[nei].add(node)
                preReq[nei].update(preReq[node])

                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return [u in preReq[v] for u,v in queries]