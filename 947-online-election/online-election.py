
from bisect import bisect_right
from typing import List
from collections import defaultdict

class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        counts = defaultdict(int)
        self.leads = []
        lead = -1
        maxcnt = 0
        for p in persons:
            counts[p] += 1
            if counts[p] >= maxcnt:
                if p != lead:
                    lead = p
                maxcnt = counts[p]
            self.leads.append(lead)

    def q(self, t: int) -> int:
        i = bisect_right(self.times, t) - 1
        return self.leads[i] if i >= 0 else -1
