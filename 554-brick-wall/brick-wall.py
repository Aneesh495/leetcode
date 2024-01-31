
from collections import defaultdict
from typing import List

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # Count how many rows have a gap at each cumulative width
        gaps = defaultdict(int)
        for row in wall:
            pos = 0
            # Skip the last brick so we do not place the line on the outer edge
            for w in row[:-1]:
                pos += w
                gaps[pos] += 1
        # If no internal gaps exist we must cross every row
        max_gaps = max(gaps.values(), default=0)
        return len(wall) - max_gaps