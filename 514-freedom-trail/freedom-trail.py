
from functools import lru_cache
from collections import defaultdict

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        # Map each character to all indices where it appears on the ring
        pos = defaultdict(list)
        for i, ch in enumerate(ring):
            pos[ch].append(i)

        # Distance on a circle between two indices
        def dist(a: int, b: int) -> int:
            d = abs(a - b)
            return min(d, n - d)

        @lru_cache(maxsize=None)
        def dp(i: int, cur: int) -> int:
            # i is index in key, cur is current 12 o'clock index on ring
            if i == len(key):
                return 0
            res = float('inf')
            for j in pos[key[i]]:
                rotate = dist(cur, j)
                # rotate steps plus 1 press plus future cost
                res = min(res, rotate + 1 + dp(i + 1, j))
            return res

        return dp(0, 0)
