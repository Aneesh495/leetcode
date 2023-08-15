
from typing import List
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Reverse flow idea
        # Start from cells that touch each ocean
        # Move only to neighbors with height not lower than current
        # Mark reachability for each ocean then intersect

        if not heights or not heights[0]:
            return []

        rows = len(heights)
        cols = len(heights[0])

        pac = [[False] * cols for _ in range(rows)]   # cells that can reach Pacific
        atl = [[False] * cols for _ in range(rows)]   # cells that can reach Atlantic
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(starts: List[tuple], seen: List[List[bool]]) -> None:
            q = deque(starts)
            for r, c in starts:
                seen[r][c] = True
            while q:
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and not seen[nr][nc]:
                        # Can flow from higher neighbor to lower current in the original problem
                        # In reverse search we require neighbor height at least current height
                        if heights[nr][nc] >= heights[r][c]:
                            seen[nr][nc] = True
                            q.append((nr, nc))

        pac_starts = [(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)]
        atl_starts = [(rows - 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows)]

        bfs(pac_starts, pac)
        bfs(atl_starts, atl)

        ans = []
        for r in range(rows):
            for c in range(cols):
                if pac[r][c] and atl[r][c]:
                    ans.append([r, c])

        return ans
