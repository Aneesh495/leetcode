
from typing import List

class NumMatrix:
    # Build a 2D prefix sum with one extra row and column of zeros
    # ps[i+1][j+1] holds the sum of submatrix (0,0) to (i,j) inclusive
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.ps = [[0]]
            return
        m, n = len(matrix), len(matrix[0])
        self.ps = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                self.ps[i + 1][j + 1] = (
                    self.ps[i][j + 1]          # sum above
                    + self.ps[i + 1][j]        # sum left
                    - self.ps[i][j]            # remove double count
                    + matrix[i][j]             # add current cell
                )

    # Return sum over rectangle [row1..row2] x [col1..col2] in O(1)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ps = self.ps
        return (
            ps[row2 + 1][col2 + 1]
            - ps[row1][col2 + 1]
            - ps[row2 + 1][col1]
            + ps[row1][col1]
        )
