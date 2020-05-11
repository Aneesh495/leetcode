
from functools import lru_cache
from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)

        @lru_cache(None)
        def dp(r1: int, c1: int, r2: int) -> int:
            c2 = r1 + c1 - r2
            if r1 >= n or c1 >= n or r2 >= n or c2 >= n:
                return -10**9
            if grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return -10**9
            if r1 == n - 1 and c1 == n - 1:
                return grid[r1][c1]
            cherries = grid[r1][c1]
            if (r1, c1) != (r2, c2):
                cherries += grid[r2][c2]
            best = max(
                dp(r1 + 1, c1, r2 + 1),  # down, down
                dp(r1, c1 + 1, r2),      # right, right
                dp(r1 + 1, c1, r2),      # down, right
                dp(r1, c1 + 1, r2 + 1)   # right, down
            )
            return cherries + best

        res = dp(0, 0, 0)
        return max(0, res)
