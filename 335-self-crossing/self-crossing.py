
from typing import List

class Solution:
    def isSelfCrossing(self, distances: List[int]) -> bool:
        # Detect crossing using three constant space cases
        # Case 1 current segment crosses the segment 3 steps before
        # Case 2 current segment meets the segment 4 steps before
        # Case 3 current segment crosses the segment 5 steps before in a spiral
        d = distances
        for i in range(3, len(d)):
            # Case 1
            if d[i] >= d[i - 2] and d[i - 1] <= d[i - 3]:
                return True
            # Case 2
            if i >= 4 and d[i - 1] == d[i - 3] and d[i] + d[i - 4] >= d[i - 2]:
                return True
            # Case 3
            if (
                i >= 5
                and d[i - 2] >= d[i - 4]
                and d[i - 1] <= d[i - 3]
                and d[i - 1] + d[i - 5] >= d[i - 3]
                and d[i] + d[i - 4] >= d[i - 2]
            ):
                return True
        return False
