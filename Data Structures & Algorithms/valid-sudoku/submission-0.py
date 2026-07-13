class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val != ".":
                    if (
                        ("row", r, val) in seen or
                        ("col", c, val) in seen or
                        ("box", r//3, c//3, val) in seen 
                    ):
                        return False
                    
                    seen.add(("row", r, val)) 
                    seen.add(("col", c, val))
                    seen.add(("box", r//3, c//3, val))
        
        return True



