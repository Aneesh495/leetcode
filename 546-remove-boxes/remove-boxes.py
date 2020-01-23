
from typing import List
from functools import lru_cache

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        """
        DP on intervals with carry count
        dp(l, r, k) returns max points for boxes[l..r] if there are k boxes equal to boxes[r]
        already attached to the right of r
        """

        @lru_cache(None)
        def dp(l: int, r: int, k: int) -> int:
            # empty interval
            if l > r:
                return 0

            # compress the tail so boxes[r] is the last of its color run
            while l < r and boxes[r] == boxes[r - 1]:
                r -= 1
                k += 1

            # option 1 remove the tail run now
            best = dp(l, r - 1, 0) + (k + 1) * (k + 1)

            # option 2 connect an earlier same color index i with the tail
            # keep boxes[i] until after removing between i and r
            for i in range(l, r):
                if boxes[i] == boxes[r]:
                    best = max(best, dp(l, i, k + 1) + dp(i + 1, r - 1, 0))

            return best

        return dp(0, len(boxes) - 1, 0)
