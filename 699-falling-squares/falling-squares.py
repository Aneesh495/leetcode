
from typing import List

class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        intervals = []  # list of (L, R, H)
        res = []
        cur_max = 0

        for l, size in positions:
            r = l + size
            h = size
            for L, R, H in intervals:
                if not (r <= L or R <= l):
                    h = max(h, H + size)
            intervals.append((l, r, h))
            cur_max = max(cur_max, h)
            res.append(cur_max)

        return res
