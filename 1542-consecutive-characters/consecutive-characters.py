class Solution:
    def maxPower(self, s: str) -> int:
        from itertools import groupby
        return max(sum(1 for _ in group) for _, group in groupby(s))