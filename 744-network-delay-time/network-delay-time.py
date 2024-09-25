
import heapq
from collections import defaultdict
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = defaultdict(list)
        for u, v, w in times:
            g[u].append((v, w))
        dist = {i: float('inf') for i in range(1, n + 1)}
        dist[k] = 0
        h = [(0, k)]
        while h:
            d, u = heapq.heappop(h)
            if d > dist[u]:
                continue
            for v, w in g[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(h, (nd, v))
        ans = max(dist.values())
        return -1 if ans == float('inf') else ans
