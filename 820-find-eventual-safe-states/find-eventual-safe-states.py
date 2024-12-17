
from typing import List
from collections import deque

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        outdeg = [len(adj) for adj in graph]
        rev = [[] for _ in range(n)]
        for u, adj in enumerate(graph):
            for v in adj:
                rev[v].append(u)
        q = deque(i for i in range(n) if outdeg[i] == 0)
        safe = [False] * n
        while q:
            u = q.popleft()
            safe[u] = True
            for p in rev[u]:
                outdeg[p] -= 1
                if outdeg[p] == 0:
                    q.append(p)
        return [i for i, ok in enumerate(safe) if ok]
