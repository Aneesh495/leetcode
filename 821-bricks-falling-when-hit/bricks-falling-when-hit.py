
class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        R, C = len(grid), len(grid[0])
        g = [row[:] for row in grid]

        # Apply hits
        effective = []
        for r, c in hits:
            if g[r][c] == 1:
                g[r][c] = 0
                effective.append(1)
            else:
                effective.append(0)

        # DSU with roof node 0, cells mapped to 1..R*C
        N = R * C + 1
        roof = 0
        parent = list(range(N))
        size = [1] * N

        def idx(r, c): return r * C + c + 1

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]

        def roof_size():
            return size[find(roof)]

        # Build DSU from grid after hits
        for r in range(R):
            for c in range(C):
                if g[r][c] == 1:
                    if r == 0:
                        union(roof, idx(r, c))
                    for dr, dc in ((1, 0), (0, 1)):
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < R and 0 <= nc < C and g[nr][nc] == 1:
                            union(idx(r, c), idx(nr, nc))

        res = []
        for k in range(len(hits) - 1, -1, -1):
            r, c = hits[k]
            if effective[k] == 0:
                res.append(0)
                continue
            pre = roof_size()
            g[r][c] = 1
            i = idx(r, c)
            if r == 0:
                union(roof, i)
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and g[nr][nc] == 1:
                    union(i, idx(nr, nc))
            post = roof_size()
            fallen = max(0, post - pre - 1)
            res.append(fallen)

        return res[::-1]
