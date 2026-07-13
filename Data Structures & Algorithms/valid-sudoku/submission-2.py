class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        boxSet = {i : set() for i in range(N)} 
        rowSet = {i : set() for i in range(N)}
        colSet = {i : set() for i in range(N)}

        for r in range(N):
            for c in range(N):

                val = board[r][c]

                if val == ".":
                    continue

                boxIdx = (r // 3) * 3 + (c // 3)
                if (
                    val in rowSet[r] or
                    val in colSet[c] or
                    val in boxSet[boxIdx]
                ):
                    return False
                
                rowSet[r].add(val)
                colSet[c].add(val)
                boxSet[boxIdx].add(val)
        
        return True