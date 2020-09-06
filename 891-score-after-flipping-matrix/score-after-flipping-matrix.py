
from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # First column can always be made all ones by flipping rows where the first bit is zero
        score = m * (1 << (n - 1))
        # For each other column count ones after considering the implied row flips
        for col in range(1, n):
            ones = 0
            for row in range(m):
                if grid[row][0] == 1:
                    ones += grid[row][col]
                else:
                    ones += 1 - grid[row][col]
            ones = max(ones, m - ones)
            score += ones * (1 << (n - 1 - col))
        return score
