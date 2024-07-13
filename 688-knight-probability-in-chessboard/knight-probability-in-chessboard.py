
from functools import lru_cache

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
        
        @lru_cache(maxsize=None)
        def dp(steps: int, r: int, c: int) -> float:
            if r < 0 or r >= n or c < 0 or c >= n:
                return 0.0
            if steps == 0:
                return 1.0
            prob = 0.0
            for dr, dc in moves:
                prob += dp(steps - 1, r + dr, c + dc)
            return prob / 8.0
        
        return dp(k, row, column)
