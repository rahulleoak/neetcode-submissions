class Solution:
    def isValid(self, row, col, m, n, board):
        return (
            0 <= row < m and
            0 <= col < n and
            board[row][col] == "O"
        )

    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        directions = [
            (0,1), (-1,0), (0,-1), (1,0)
        ]

        def dfs(row, col):
            if not self.isValid(row, col, m, n, board):
                return 
            
            board[row][col] = "S" # Safe since its connected to a border cell

            for dr, dc in directions:
                nr, nc = dr + row, dc + col
                dfs(nr,nc)
        
        for r in range(m):
            if board[r][0] == "O":
                dfs(r,0)
            if board[r][n-1] == "O":
                dfs(r,n-1)

        for c in range(n):
            if board[0][c] == "O":
                dfs(0,c)
            if board[m-1][c] == "O":
                dfs(m-1,c)

        for r in range(0, m):
            for c in range(0, n):
                if board[r][c] == "S":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
    
        