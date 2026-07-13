class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {i : [] for i in range(numCourses)}
        for course, req in prerequisites:
            adjList[req].append(course)
        
        visited = [None] * numCourses
        topoOrder = []

        def dfs(node):
            if visited[node] is not None:
                return visited[node]
            
            visited[node] = False
            for nei in adjList[node]:
                if visited[nei] == None:
                    if not dfs(nei):
                        return False
                elif visited[nei] == False:
                    return False
            
            visited[node] = True
            topoOrder.append(node)
            return True

        for node in range(numCourses):
            if visited[node] is None and not dfs(node):
                return []
        
        return topoOrder[::-1]