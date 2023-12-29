
from functools import lru_cache

class Solution:
    def countArrangement(self, n: int) -> int:
        """
        Backtracking with memoization using a bit mask.
        pos is the current position in the permutation. Positions are one indexed.
        used stores which numbers are already placed. Bit i means number i plus 1 is used.
        We try every number that satisfies the divisibility rule for this position.
        Caching on (pos, used) avoids recomputation. This runs fast for n up to 15.
        """
        @lru_cache(maxsize=None)
        def dfs(pos: int, used: int) -> int:
            if pos == n + 1:
                return 1
            total = 0
            for num in range(1, n + 1):
                if not (used >> (num - 1)) & 1:
                    if num % pos == 0 or pos % num == 0:
                        total += dfs(pos + 1, used | (1 << (num - 1)))
            return total

        return dfs(1, 0)
