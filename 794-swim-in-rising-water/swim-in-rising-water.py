
from typing import List
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = [(grid[0][0], 0, 0)]
        visited = [[False]*n for _ in range(n)]
        ans = 0
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while heap:
            t, r, c = heapq.heappop(heap)
            if visited[r][c]:
                continue
            visited[r][c] = True
            ans = max(ans, t)
            if r == n - 1 and c == n - 1:
                return ans
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    heapq.heappush(heap, (grid[nr][nc], nr, nc))
        
        return ans
