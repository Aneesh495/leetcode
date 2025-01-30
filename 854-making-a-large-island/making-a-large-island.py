
from typing import List
from collections import deque, defaultdict

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 0:
            return 0

        def bfs(sr: int, sc: int, idx: int) -> int:
            q = deque([(sr, sc)])
            grid[sr][sc] = idx
            area = 1
            while q:
                r, c = q.popleft()
                for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = idx
                        area += 1
                        q.append((nr, nc))
            return area

        idx = 2
        area_map = {0: 0}
        has_zero = False
        ans = 0

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    area = bfs(r, c, idx)
                    area_map[idx] = area
                    ans = max(ans, area)
                    idx += 1
                elif grid[r][c] == 0:
                    has_zero = True

        if not has_zero:
            return ans if ans else n * n

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen = set()
                    cur = 1
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n:
                            comp = grid[nr][nc]
                            if comp > 1 and comp not in seen:
                                seen.add(comp)
                                cur += area_map[comp]
                    ans = max(ans, cur)

        return ans
