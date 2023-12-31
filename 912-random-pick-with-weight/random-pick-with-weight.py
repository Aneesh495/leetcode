
from typing import List
from bisect import bisect_left
import random

class Solution:
    def __init__(self, w: List[int]):
        # Build prefix sums so each index occupies a range proportional to its weight
        self.prefix = []
        running = 0
        for x in w:
            running += x
            self.prefix.append(running)
        self.total = running  # total weight

    def pickIndex(self) -> int:
        # Pick an integer in [1, total] uniformly
        target = random.randint(1, self.total)
        # Find the first prefix sum that is >= target
        return bisect_left(self.prefix, target)
