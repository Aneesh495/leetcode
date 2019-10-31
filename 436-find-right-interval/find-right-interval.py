
from typing import List
import bisect

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # Build a list of (start, original_index) then sort by start
        starts = sorted((intervals[i][0], i) for i in range(len(intervals)))
        start_vals = [s for s, _ in starts]

        res = [-1] * len(intervals)
        for i, (_, end) in enumerate(intervals):
            # Find the first start that is >= current end
            j = bisect.bisect_left(start_vals, end)
            res[i] = starts[j][1] if j < len(starts) else -1
        return res
