
from collections import deque
from typing import List

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        q = deque()

        def inb(i,j):
            return 0 <= i < n and 0 <= j < n

        def dfs(i,j):
            if not inb(i,j) or grid[i][j] != 1:
                return
            grid[i][j] = -1
            q.append((i,j))
            for di,dj in dirs:
                dfs(i+di, j+dj)

        found = False
        for i in range(n):
            if found:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i,j)
                    found = True
                    break

        steps = 0
        while q:
            for _ in range(len(q)):
                i,j = q.popleft()
                for di,dj in dirs:
                    ni, nj = i+di, j+dj
                    if not inb(ni,nj) or grid[ni][nj] == -1:
                        continue
                    if grid[ni][nj] == 1:
                        return steps
                    grid[ni][nj] = -1
                    q.append((ni,nj))
            steps += 1
        return -1
