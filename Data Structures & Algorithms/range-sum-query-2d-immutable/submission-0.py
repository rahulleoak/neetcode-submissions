class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.rowRange, self.colRange = len(matrix), len(matrix[0])
        self.matrixSum = [[0] * (self.colRange + 1) for _ in range(self.rowRange + 1)]

        for r in range(self.rowRange):
            prefix = 0
            for c in range(self.colRange):
                prefix += matrix[r][c]
                above = self.matrixSum[r][c+1]
                self.matrixSum[r+1][c+1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1 = row1 + 1, col1 + 1
        row2, col2 = row2 + 1, col2 + 1

        bottomRight = self.matrixSum[row2][col2]
        above = self.matrixSum[row1-1][col2]
        left = self.matrixSum[row2][col1-1]
        topLeft = self.matrixSum[row1-1][col1-1]

        return bottomRight - above - left + topLeft
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)