
from typing import List

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        # Count all non obstacle squares and locate start
        total = 0
        sx = sy = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != -1:
                    total += 1
                if grid[i][j] == 1:
                    sx, sy = i, j

        def dfs(x: int, y: int, remain: int) -> int:
            # If we reached the end then check if we visited all squares
            if grid[x][y] == 2:
                return 1 if remain == 1 else 0

            # Mark current square visited
            temp = grid[x][y]
            grid[x][y] = -2  # visited marker

            paths = 0
            for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
                nx = x + dx
                ny = y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != -1 and grid[nx][ny] != -2:
                    paths += dfs(nx, ny, remain - 1)

            # Backtrack
            grid[x][y] = temp
            return paths

        return dfs(sx, sy, total)
