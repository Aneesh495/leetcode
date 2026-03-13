
from typing import List
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g = [[] for _ in range(n)]
        for u, v, w in flights:
            g[u].append((v, w))

        INF = 10**15
        best = [[INF] * (k + 2) for _ in range(n)]
        best[src][0] = 0

        heap = [(0, src, 0)]  # cost, node, stops_used
        while heap:
            cost, u, s = heapq.heappop(heap)
            if u == dst:
                return cost
            if s == k + 1:
                continue
            for v, w in g[u]:
                nc = cost + w
                ns = s + 1
                if nc < best[v][ns]:
                    best[v][ns] = nc
                    heapq.heappush(heap, (nc, v, ns))
        return -1
