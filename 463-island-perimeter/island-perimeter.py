
from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Perimeter starts at 0
        perimeter = 0
        rows = len(grid)
        cols = len(grid[0]) if rows else 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # Each land cell contributes 4 sides
                    perimeter += 4

                    # Subtract 2 for each shared edge
                    # Check cell above
                    if r > 0 and grid[r - 1][c] == 1:
                        perimeter -= 2
                    # Check cell to the left
                    if c > 0 and grid[r][c - 1] == 1:
                        perimeter -= 2

        return perimeter
