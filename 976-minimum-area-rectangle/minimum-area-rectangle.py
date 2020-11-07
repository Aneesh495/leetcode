
from typing import List
from collections import defaultdict

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        cols = defaultdict(list)
        for x, y in points:
            cols[x].append(y)
        last = {}
        ans = float('inf')
        for x in sorted(cols.keys()):
            ys = sorted(cols[x])
            for i in range(len(ys)):
                y1 = ys[i]
                for j in range(i + 1, len(ys)):
                    y2 = ys[j]
                    key = (y1, y2)
                    if key in last:
                        ans = min(ans, (x - last[key]) * (y2 - y1))
                    last[key] = x
        return 0 if ans == float('inf') else ans
