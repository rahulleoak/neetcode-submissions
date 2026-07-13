class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def isValid(r, c):
            return (
                0 <= r < ROWS and
                0 <= c < COLS and
                board[r][c] == "O"
            )
        
        def dfs(r,c):
            if not isValid(r,c):
                return
            
            board[r][c] = "S"

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                dfs(nr,nc)
        
        ROWS, COLS = len(board), len(board[0])
        directions = [
            (0,1), (1,0), (0,-1), (-1,0)
        ]

        for r in range(ROWS):
            if board[r][0] == "O":
                dfs(r,0)
            if board[r][COLS - 1] == "O":
                dfs(r, COLS-1)

        for c in range(COLS):
            if board[0][c] == "O":
                dfs(0,c)
            if board[ROWS - 1][c] == "O":
                dfs(ROWS-1,c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "S":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
        