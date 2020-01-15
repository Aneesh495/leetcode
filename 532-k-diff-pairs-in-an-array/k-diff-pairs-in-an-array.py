
from typing import List
from collections import Counter

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # Negative k cannot produce an absolute difference
        if k < 0:
            return 0

        # k equals zero means we count values that appear at least twice
        if k == 0:
            freq = Counter(nums)
            return sum(1 for v in freq.values() if v > 1)

        # k greater than zero means count unique x where x + k exists
        seen = set(nums)
        return sum(1 for x in seen if x + k in seen)
