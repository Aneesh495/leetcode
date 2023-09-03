
from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Greedy
        Pick as many non overlapping intervals as possible by sorting by end time
        Minimum removals equals total intervals minus the number we can keep
        """
        if not intervals:
            return 0

        # Sort by end time to always keep the interval that frees the timeline earliest
        intervals.sort(key=lambda x: x[1])

        kept = 0
        prev_end = float("-inf")

        for start, end in intervals:
            # If current interval starts after or at the end of the last kept interval
            # we can keep it and update the end marker
            if start >= prev_end:
                kept += 1
                prev_end = end
            # Else we skip it which means it is effectively removed

        return len(intervals) - kept
