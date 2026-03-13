
from typing import List

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first = {}
        last = {}
        freq = {}
        for i, x in enumerate(nums):
            if x not in first:
                first[x] = i
            last[x] = i
            freq[x] = freq.get(x, 0) + 1

        degree = max(freq.values())
        best = len(nums)
        for x, cnt in freq.items():
            if cnt == degree:
                best = min(best, last[x] - first[x] + 1)
        return best
