
from typing import List
import bisect

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """
        Russian Doll Envelopes
        Sort by width asc and height desc for equal widths
        Then find LIS on heights using patience sorting in O(n log n)
        """
        if not envelopes:
            return 0

        # Sort ensures envelopes with same width do not chain
        # because higher height comes first and will be replaced in LIS
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        tails: List[int] = []  # tails[i] stores the smallest tail of an LIS of length i+1

        for _, h in envelopes:
            # Find insertion point for h in tails
            i = bisect.bisect_left(tails, h)
            if i == len(tails):
                # Extend LIS
                tails.append(h)
            else:
                # Improve smaller tail for same length
                tails[i] = h

        return len(tails)
