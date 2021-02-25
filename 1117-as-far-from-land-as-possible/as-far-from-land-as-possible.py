from collections import deque
from typing import List

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    q.append((r, c))

        if not q or len(q) == n * n:
            return -1

        dist = -1
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            dist += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        q.append((nr, nc))

        return dist