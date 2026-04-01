
from typing import List

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # Track longest subarray ending at current index where last comparison is up or down
        up = 1          # length ending at i with arr[i-1] < arr[i]
        down = 1        # length ending at i with arr[i-1] > arr[i]
        best = 1

        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                # Extend a sequence that last went down
                up = down + 1
                down = 1
            elif arr[i] < arr[i - 1]:
                # Extend a sequence that last went up
                down = up + 1
                up = 1
            else:
                # Equal breaks turbulence
                up = 1
                down = 1
            best = max(best, up, down)

        return best
