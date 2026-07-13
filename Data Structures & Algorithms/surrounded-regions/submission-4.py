class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def isValid(r,c):
            return (
                0 <= r < R and 
                0 <= c < C and 
                board[r][c] == "O"
            )
        
        def dfs(r,c):
            if not isValid(r,c):
                return 
            
            board[r][c] = "S"

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                dfs(nr,nc)


        R, C = len(board), len(board[0])
        directions = [
            (0,1), (0,-1), (1,0), (-1,0)
        ]

        for r in range(R):
            if board[r][0] == "O":
                dfs(r,0)
            if board[r][C-1] == "O":
                dfs(r,C-1)
        
        for c in range(C):
            if board[0][c] == "O":
                dfs(0,c)
            if board[R-1][c] == "O":
                dfs(R-1,c)
        

        for r in range(R):
            for c in range(C):
                if board[r][c] == "S":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
        