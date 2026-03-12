
from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        buckets = [0] * (n + 1)
        for c in citations:
            buckets[min(c, n)] += 1
        papers = 0
        for h in range(n, -1, -1):
            papers += buckets[h]
            if papers >= h:
                return h
        return 0
