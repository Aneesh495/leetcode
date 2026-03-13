
from collections import deque
from typing import List

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = [[] for _ in range(n + 1)]
        for a, b in dislikes:
            adj[a].append(b)
            adj[b].append(a)
        color = [0] * (n + 1)  # 0 uncolored, 1 and -1 are the two groups
        for i in range(1, n + 1):
            if color[i] != 0:
                continue
            color[i] = 1
            q = deque([i])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = -color[u]
                        q.append(v)
                    elif color[v] == color[u]:
                        return False
        return True
