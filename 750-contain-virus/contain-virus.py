
from typing import List

class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        m, n = len(isInfected), len(isInfected[0])
        ans = 0

        def neighbors(r, c):
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    yield nr, nc

        while True:
            seen = [[False]*n for _ in range(m)]
            regions = []
            frontiers = []
            walls_needed = []

            for r in range(m):
                for c in range(n):
                    if isInfected[r][c] == 1 and not seen[r][c]:
                        stack = [(r, c)]
                        seen[r][c] = True
                        region = []
                        frontier = set()
                        walls = 0
                        while stack:
                            x, y = stack.pop()
                            region.append((x, y))
                            for nx, ny in neighbors(x, y):
                                if isInfected[nx][ny] == 0:
                                    walls += 1
                                    frontier.add((nx, ny))
                                elif isInfected[nx][ny] == 1 and not seen[nx][ny]:
                                    seen[nx][ny] = True
                                    stack.append((nx, ny))
                        regions.append(region)
                        frontiers.append(frontier)
                        walls_needed.append(walls)

            if not regions:
                break

            idx = 0
            max_threat = 0
            for i, f in enumerate(frontiers):
                if len(f) > max_threat:
                    max_threat = len(f)
                    idx = i

            if max_threat == 0:
                break

            ans += walls_needed[idx]

            for x, y in regions[idx]:
                isInfected[x][y] = 2

            for i, f in enumerate(frontiers):
                if i == idx:
                    continue
                for x, y in f:
                    if isInfected[x][y] == 0:
                        isInfected[x][y] = 1
        return ans
