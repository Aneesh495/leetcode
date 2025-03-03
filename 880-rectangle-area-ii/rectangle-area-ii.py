
from typing import List

class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        MOD = 10**9 + 7
        ys = sorted({y for _, y1, _, y2 in rectangles for y in (y1, y2)})
        y_i = {y:i for i, y in enumerate(ys)}
        events = []
        for x1, y1, x2, y2 in rectangles:
            if x1 < x2 and y1 < y2:
                events.append((x1, y1, y2, 1))
                events.append((x2, y1, y2, -1))
        events.sort()
        n = len(ys) - 1
        cover = [0]*(4*n)
        length = [0]*(4*n)

        def update(i, l, r, ql, qr, val):
            if ql >= r or qr <= l:
                return
            if ql <= l and r <= qr:
                cover[i] += val
            else:
                m = (l + r) // 2
                update(i*2, l, m, ql, qr, val)
                update(i*2+1, m, r, ql, qr, val)
            if cover[i] > 0:
                length[i] = ys[r] - ys[l]
            else:
                length[i] = (length[i*2] + length[i*2+1]) if r - l > 1 else 0

        prev_x = events[0][0] if events else 0
        area = 0
        for x, y1, y2, typ in events:
            area = (area + length[1] * (x - prev_x)) % MOD
            update(1, 0, n, y_i[y1], y_i[y2], typ)
            prev_x = x
        return area % MOD
