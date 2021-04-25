class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        for r in matrix:
            for c in range(1, len(r)):
                r[c] += r[c-1]
        self.matrix = matrix
        

    def update(self, row: int, col: int, val: int) -> None:
        original = self.matrix[row][col]
        if col!=0:
            original -= self.matrix[row][col-1]
        diff = original - val
        for c in range(col, len(self.matrix[0])):
            self.matrix[row][c] -= diff

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sums = 0
        for r in range(row1, row2+1):
            sums += self.matrix[r][col2]
            if  col1 != 0:
                sums -= self.matrix[r][col1-1]
        return sums
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)