
from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # Greedy left to right
        # keep track of which adjacent row pairs are already strictly ordered
        m = len(strs)
        n = len(strs[0])
        ordered = [False] * (m - 1)
        deletions = 0

        for c in range(n):
            # Check if keeping this column would break order for any unresolved pair
            bad = False
            for i in range(m - 1):
                if not ordered[i] and strs[i][c] > strs[i + 1][c]:
                    bad = True
                    break

            if bad:
                deletions += 1
                continue

            # Safe to keep this column
            # Mark pairs that become strictly ordered thanks to this column
            for i in range(m - 1):
                if not ordered[i] and strs[i][c] < strs[i + 1][c]:
                    ordered[i] = True

            # Early exit if all pairs are ordered
            if all(ordered):
                break

        return deletions
