
from typing import List
from collections import Counter

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        vals = sorted(cnt)
        prev = None
        take = skip = 0
        for v in vals:
            earn = v * cnt[v]
            if prev is not None and v == prev + 1:
                take, skip = skip + earn, max(take, skip)
            else:
                best = max(take, skip)
                take, skip = best + earn, best
            prev = v
        return max(take, skip)
