
from collections import deque
from typing import List

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        if n == 1:
            return 0
        target = (1 << n) - 1
        q = deque()
        seen = [[False] * (1 << n) for _ in range(n)]
        for i in range(n):
            mask = 1 << i
            q.append((i, mask))
            seen[i][mask] = True
        steps = 0
        while q:
            for _ in range(len(q)):
                u, mask = q.popleft()
                for v in graph[u]:
                    m2 = mask | (1 << v)
                    if m2 == target:
                        return steps + 1
                    if not seen[v][m2]:
                        seen[v][m2] = True
                        q.append((v, m2))
            steps += 1
        return -1
