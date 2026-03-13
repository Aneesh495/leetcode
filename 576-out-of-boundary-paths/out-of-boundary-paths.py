
from functools import lru_cache

MOD = 10**9 + 7

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @lru_cache(None)
        def dfs(r: int, c: int, k: int) -> int:
            if r < 0 or r >= m or c < 0 or c >= n:
                return 1
            if k == 0:
                return 0
            res = 0
            res += dfs(r + 1, c, k - 1)
            res += dfs(r - 1, c, k - 1)
            res += dfs(r, c + 1, k - 1)
            res += dfs(r, c - 1, k - 1)
            return res % MOD

        return dfs(startRow, startColumn, maxMove) % MOD
