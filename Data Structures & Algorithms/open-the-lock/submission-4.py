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
        
        begin = {"0000"}
        end = {target}
        turns = 0

        while begin and end:
            if len(begin) > len(end):
                begin, end = end, begin
    
            newState = set()

            for state in begin:
                for move in movements(state):
                    if move in end:
                        return turns + 1
                    if move in visited:
                        continue
                    
                    visited.add(move)
                    newState.add(move)

            turns += 1
            begin = newState                    


        return -1
