
import random
import bisect
from typing import List

class Solution:
    # Precompute prefix sums of counts of integer lattice points per rectangle
    # Each rectangle is [x1, y1, x2, y2] inclusive
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.prefix = []
        total = 0
        for x1, y1, x2, y2 in rects:
            cnt = (x2 - x1 + 1) * (y2 - y1 + 1)  # number of integer points
            total += cnt
            self.prefix.append(total)

    # Pick a random point with uniform probability over all integer points
    def pick(self) -> List[int]:
        # Choose a global rank in [1, total]
        r = random.randint(1, self.prefix[-1])
        # Find the rectangle that contains this rank
        idx = bisect.bisect_left(self.prefix, r)
        x1, y1, x2, y2 = self.rects[idx]
        # Choose a random integer point inside the chosen rectangle
        x = random.randint(x1, x2)
        y = random.randint(y1, y2)
        return [x, y]
