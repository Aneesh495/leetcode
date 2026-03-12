
from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # Multi source BFS starting from all zeros
        m = len(mat)
        n = len(mat[0])
        INF = 10**9
        
        dist = [[INF] * n for _ in range(m)]
        q = deque()
        
        # Initialize queue with all zero cells
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    q.append((i, j))
        
        # Four neighbor directions
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # BFS to relax distances
        while q:
            i, j = q.popleft()
            for di, dj in dirs:
                ni = i + di
                nj = j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    # If we can improve neighbor distance by going through current cell
                    if dist[ni][nj] > dist[i][j] + 1:
                        dist[ni][nj] = dist[i][j] + 1
                        q.append((ni, nj))
        
        return dist
