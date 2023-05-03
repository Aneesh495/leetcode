
from functools import lru_cache
from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # Edge case guard
        if not matrix or not matrix[0]:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        # Four movement directions
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        @lru_cache(None)
        def dfs(r: int, c: int) -> int:
            # Length of the longest path starting at cell r c
            best = 1  # at least the cell itself
            curr = matrix[r][c]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                # Move only inside bounds and to a strictly greater value
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > curr:
                    best = max(best, 1 + dfs(nr, nc))
            return best

        ans = 0
        for r in range(rows):
            for c in range(cols):
                ans = max(ans, dfs(r, c))
        return ans
