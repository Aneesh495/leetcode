
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows = len(matrix)
        cols = len(matrix[0])

        r = 0
        c = cols - 1

        while r < rows and c >= 0:
            val = matrix[r][c]
            if val == target:
                return True
            if val > target:
                c -= 1
            else:
                r += 1

        return False
