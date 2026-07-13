class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        row = {i : set() for i in range(N)}
        col = {i : set() for i in range(N)}
        box = {i : set() for i in range(N)}

        for r in range(N):
            for c in range(N):
                val = board[r][c]

                if val == ".":
                    continue
                
                boxIdx = (r//3) * 3 + (c//3)
                if (
                    val in row[r] or
                    val in col[c] or 
                    val in box[boxIdx]
                ):
                    return False

                row[r].add(val)
                col[c].add(val)
                box[boxIdx].add(val)

        return True