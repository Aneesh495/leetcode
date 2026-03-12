
import heapq
from typing import List

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        # Min heap holds tuples of (height, row, col)
        # Start from the boundary which defines the initial water level
        if not heightMap or not heightMap[0]:
            return 0
        m = len(heightMap)
        n = len(heightMap[0])
        if m < 3 or n < 3:
            return 0

        visited = [[False] * n for _ in range(m)]
        heap = []

        # Add all boundary cells to the heap
        for r in range(m):
            for c in (0, n - 1):
                heapq.heappush(heap, (heightMap[r][c], r, c))
                visited[r][c] = True
        for c in range(n):
            for r in (0, m - 1):
                if not visited[r][c]:
                    heapq.heappush(heap, (heightMap[r][c], r, c))
                    visited[r][c] = True

        water = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Process cells in increasing boundary height
        while heap:
            h, r, c = heapq.heappop(heap)
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    nh = heightMap[nr][nc]
                    # If neighbor lower than current boundary, water is trapped
                    if nh < h:
                        water += h - nh
                    # The effective boundary becomes max of current boundary and neighbor height
                    heapq.heappush(heap, (max(h, nh), nr, nc))

        return water
