class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        terminal = set(deadends)
        if "0000" in terminal or target in terminal:
            return -1
        if "0000" == target:
            return 0
        
        def neighbours(combo):
            for i in range(4):
                val = int(combo[i])

                for shift in [-1,1]:
                    change = (val + shift) % 10
                    yield combo[:i] + str(change) + combo[i+1:]
        
        START = {"0000"}
        END = {target}
        terminal = terminal | START | END

        steps = 0
        while START and END:
            if len(START) > len(END):
                START, END = END, START
            
            steps += 1
            
            nextLayer = set()
            for combo in START:
                for nei in neighbours(combo):
                    if nei in END:
                        return steps
                    if nei not in terminal:
                        terminal.add(nei)
                        nextLayer.add(nei)
            
            START = nextLayer

        return -1