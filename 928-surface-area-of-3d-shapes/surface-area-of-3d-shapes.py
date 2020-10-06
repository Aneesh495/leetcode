
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        area = 0
        for i in range(n):
            for j in range(n):
                v = grid[i][j]
                if v:
                    area += 4 * v + 2
                if i + 1 < n:
                    area -= 2 * min(v, grid[i + 1][j])
                if j + 1 < n:
                    area -= 2 * min(v, grid[i][j + 1])
        return area
