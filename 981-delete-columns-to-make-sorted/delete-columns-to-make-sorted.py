
from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        if not strs:
            return 0
        cols = len(strs[0])
        deletions = 0
        for c in range(cols):
            for r in range(1, len(strs)):
                if strs[r][c] < strs[r - 1][c]:
                    deletions += 1
                    break
        return deletions
