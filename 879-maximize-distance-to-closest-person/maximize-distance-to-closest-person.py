
from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        prev = -1
        ans = 0
        for i, v in enumerate(seats):
            if v == 1:
                if prev == -1:
                    ans = i
                else:
                    ans = max(ans, (i - prev) // 2)
                prev = i
        ans = max(ans, len(seats) - 1 - prev)
        return ans
