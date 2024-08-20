
import bisect
from math import inf

class RangeModule:
    def __init__(self):
        self.intervals = []  # list of [l, r), disjoint and sorted by l

    def addRange(self, left: int, right: int) -> None:
        new_iv = []
        placed = False
        for l, r in self.intervals:
            if r < left:
                new_iv.append([l, r])
            elif right < l:
                if not placed:
                    new_iv.append([left, right])
                    placed = True
                new_iv.append([l, r])
            else:
                left = min(left, l)
                right = max(right, r)
        if not placed:
            new_iv.append([left, right])
        self.intervals = new_iv

    def queryRange(self, left: int, right: int) -> bool:
        i = bisect.bisect_right(self.intervals, [left, inf]) - 1
        if i >= 0:
            l, r = self.intervals[i]
            return l <= left and right <= r
        return False

    def removeRange(self, left: int, right: int) -> None:
        new_iv = []
        for l, r in self.intervals:
            if r <= left or right <= l:
                new_iv.append([l, r])
            else:
                if l < left:
                    new_iv.append([l, left])
                if right < r:
                    new_iv.append([right, r])
        self.intervals = new_iv
