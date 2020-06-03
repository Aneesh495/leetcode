
# Definition for a QuadTree node.
# class Node:
#     def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
#         self.val = val
#         self.isLeaf = isLeaf
#         self.topLeft = topLeft
#         self.topRight = topRight
#         self.bottomLeft = bottomLeft
#         self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)

        # Build 2D prefix sum of grid
        # ps[r+1][c+1] holds sum of submatrix grid[0..r][0..c]
        ps = [[0] * (n + 1) for _ in range(n + 1)]
        for r in range(n):
            row_sum = 0
            for c in range(n):
                row_sum += grid[r][c]
                ps[r + 1][c + 1] = ps[r][c + 1] + row_sum

        # Return sum of square submatrix starting at (r0, c0) with side size sz
        def region_sum(r0: int, c0: int, sz: int) -> int:
            r1 = r0 + sz
            c1 = c0 + sz
            return ps[r1][c1] - ps[r0][c1] - ps[r1][c0] + ps[r0][c0]

        def build(r0: int, c0: int, sz: int) -> 'Node':
            total = region_sum(r0, c0, sz)
            if total == 0 or total == sz * sz:
                # All zeros or all ones
                return Node(val=bool(total), isLeaf=True,
                            topLeft=None, topRight=None,
                            bottomLeft=None, bottomRight=None)
            half = sz // 2
            tl = build(r0, c0, half)
            tr = build(r0, c0 + half, half)
            bl = build(r0 + half, c0, half)
            br = build(r0 + half, c0 + half, half)
            return Node(val=True, isLeaf=False,
                        topLeft=tl, topRight=tr,
                        bottomLeft=bl, bottomRight=br)

        return build(0, 0, n)
