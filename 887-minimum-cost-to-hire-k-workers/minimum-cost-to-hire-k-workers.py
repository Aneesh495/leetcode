
from typing import List
import heapq

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = sorted(((w / q, q) for q, w in zip(quality, wage)))
        max_heap = []
        qsum = 0
        ans = float('inf')
        for ratio, q in workers:
            heapq.heappush(max_heap, -q)
            qsum += q
            if len(max_heap) > k:
                qsum += heapq.heappop(max_heap)
            if len(max_heap) == k:
                ans = min(ans, qsum * ratio)
        return ans
