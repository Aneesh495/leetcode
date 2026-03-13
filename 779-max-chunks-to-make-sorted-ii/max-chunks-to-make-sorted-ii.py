
from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        prefix_max = [0]*n
        cur = float("-inf")
        for i in range(n):
            cur = max(cur, arr[i])
            prefix_max[i] = cur

        suffix_min = [float("inf")]*(n+1)
        for i in range(n-1, -1, -1):
            suffix_min[i] = min(suffix_min[i+1], arr[i])

        chunks = 0
        for i in range(n):
            if prefix_max[i] <= suffix_min[i+1]:
                chunks += 1
        return chunks
