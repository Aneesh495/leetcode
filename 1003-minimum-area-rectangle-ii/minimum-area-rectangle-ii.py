
# LeetCode 963. Minimum Area Rectangle II
# Time: O(n^2) over point pairs
# Idea:
#   Any rectangle’s diagonals share the same midpoint and the same length.
#   For each pair of points (as a potential diagonal), group by:
#     - midpoint encoded as integer pair (x1 + x2, y1 + y2) to avoid floats
#     - squared length of the diagonal
#   Inside each group, every two pairs form a rectangle with vertices (a,b,c,d).
#   Area = |a - c| * |a - d| where |.| is Euclidean distance.

from typing import List
import math
from collections import defaultdict

class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        n = len(points)
        pts = [(x, y) for x, y in points]

        groups = defaultdict(list)
        # Build groups keyed by (midpoint_x_times_2, midpoint_y_times_2, diagonal_len_sq)
        for i in range(n):
            x1, y1 = pts[i]
            for j in range(i + 1, n):
                x2, y2 = pts[j]
                mx2 = x1 + x2                  # midpoint x multiplied by 2
                my2 = y1 + y2                  # midpoint y multiplied by 2
                d2 = (x1 - x2) ** 2 + (y1 - y2) ** 2
                groups[(mx2, my2, d2)].append((i, j))

        ans = math.inf

        # For each group, combine every two diagonals
        for pairs in groups.values():
            m = len(pairs)
            if m < 2:
                continue
            # Compare each pair with previous pairs in the same group
            for a in range(m):
                i1, j1 = pairs[a]
                ax, ay = pts[i1]
                bx, by = pts[j1]
                for b in range(a):
                    i2, j2 = pairs[b]
                    cx, cy = pts[i2]
                    dx, dy = pts[j2]
                    # Rectangle vertices are {A,B,C,D} = {ax,ay}, {bx,by}, {cx,cy}, {dx,dy}
                    # Choose A as one vertex. Adjacent sides are AC and AD.
                    ac2 = (ax - cx) ** 2 + (ay - cy) ** 2
                    ad2 = (ax - dx) ** 2 + (ay - dy) ** 2
                    area = math.sqrt(ac2) * math.sqrt(ad2)
                    if area < ans and area > 0:
                        ans = area

        return 0.0 if ans == math.inf else ans
