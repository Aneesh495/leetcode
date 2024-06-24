
from typing import List
from collections import deque

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        if not forest or not forest[0]:
            return -1

        rows, cols = len(forest), len(forest[0])

        # Collect all trees (height > 1) with their positions, sorted by height
        trees = []
        for r in range(rows):
            for c in range(cols):
                if forest[r][c] > 1:
                    trees.append((forest[r][c], r, c))
        trees.sort()

        def bfs(sr: int, sc: int, tr: int, tc: int) -> int:
            if sr == tr and sc == tc:
                return 0
            if forest[sr][sc] == 0 or forest[tr][tc] == 0:
                return -1
            q = deque([(sr, sc, 0)])
            seen = {(sr, sc)}
            while q:
                r, c, d = q.popleft()
                for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and forest[nr][nc] != 0 and (nr, nc) not in seen:
                        if nr == tr and nc == tc:
                            return d + 1
                        seen.add((nr, nc))
                        q.append((nr, nc, d + 1))
            return -1

        total_steps = 0
        cr = cc = 0
        for _, tr, tc in trees:
            dist = bfs(cr, cc, tr, tc)
            if dist == -1:
                return -1
            total_steps += dist
            cr, cc = tr, tc
            forest[tr][tc] = 1  # cut the tree

        return total_steps
