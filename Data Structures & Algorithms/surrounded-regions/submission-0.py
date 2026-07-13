class Solution:
    def capture(self, grid, row, col):
        if (
            row < 0 or row >= self.ROWS or 
            col < 0 or col >= self.COLS or
            grid[row][col] != 'O'
        ):
            return
        
        grid[row][col] = 'U'

        for dr, dc in self.directions:
            nr , nc = dr + row , dc + col
            self.capture(grid,nr,nc)

    def solve(self, board: List[List[str]]) -> None:
        self.ROWS , self.COLS = len(board), len(board[0])
        self.directions = [
            (0,1), (1,0), (-1,0), (0,-1)
        ]

        for r in range(self.ROWS):
            if board[r][0] == "O":
                self.capture(board,r,0)
            if board[r][self.COLS - 1] == "O":
                self.capture(board,r,self.COLS - 1)
        
        for c in range(self.COLS):
            if board[0][c] == "O":
                self.capture(board,0,c)
            if board[self.ROWS - 1][c] == "O":
                self.capture(board,self.ROWS - 1,c)
        

        for r in range(self.ROWS):
            for c in range(self.COLS):
                if board[r][c] == "U":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
        