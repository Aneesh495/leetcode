
from typing import List

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        size = n * n * 4  # 4 triangles per cell: 0 top 1 right 2 bottom 3 left
        parent = list(range(size))
        rank = [0] * size

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if rank[ra] < rank[rb]:
                parent[ra] = rb
            elif rank[ra] > rank[rb]:
                parent[rb] = ra
            else:
                parent[rb] = ra
                rank[ra] += 1

        for r in range(n):
            for c in range(n):
                base = (r * n + c) * 4
                ch = grid[r][c]
                # internal unions
                if ch == ' ':
                    union(base + 0, base + 1)
                    union(base + 1, base + 2)
                    union(base + 2, base + 3)
                elif ch == '/':
                    union(base + 0, base + 3)
                    union(base + 1, base + 2)
                else:  # ch == '\\'
                    union(base + 0, base + 1)
                    union(base + 2, base + 3)
                # neighbor unions
                if r + 1 < n:
                    down_base = ((r + 1) * n + c) * 4
                    union(base + 2, down_base + 0)
                if c + 1 < n:
                    right_base = (r * n + c + 1) * 4
                    union(base + 1, right_base + 3)

        # count unique roots
        roots = set(find(i) for i in range(size))
        return len(roots)
