class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000":
            return 0
               
        visited = set(deadends)
        if "0000" in visited:
            return -1

        def movements(state):
            for i in range(4):
                digit = int(state[i])
                for move in [-1, 1]:
                    newState = (digit + move) % 10
                    yield state[:i] + str(newState) + state[i+1:]
        
        state = "0000"
        turns = 0
        q = deque([(state, turns)])
        visited.add(state)

        
        while q:
            curr, turnCount = q.popleft()

            for newState in movements(curr):
                if newState in visited:
                    continue
                if newState == target:
                    return turnCount + 1
                
                visited.add(newState)
                q.append((newState, turnCount + 1))
        
        return -1
