
from typing import List

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        res = 0
        s1, s2 = -1, -1  # two largest selected points so far

        for l, r in intervals:
            if l > s2:
                # no selected points in [l, r]
                res += 2
                s1, s2 = r - 1, r
            elif l > s1:
                # exactly one selected point in [l, r] (s2)
                res += 1
                s1, s2 = s2, r
            # else already have two points inside, do nothing

        return res
