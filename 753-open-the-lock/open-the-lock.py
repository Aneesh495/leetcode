
from typing import List
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        start = "0000"
        if start in dead:
            return -1
        if target == start:
            return 0

        def neighbors(s: str):
            for i in range(4):
                d = int(s[i])
                for move in (-1, 1):
                    nd = (d + move) % 10
                    yield s[:i] + str(nd) + s[i+1:]

        q = deque([(start, 0)])
        visited = {start}

        while q:
            state, dist = q.popleft()
            for nxt in neighbors(state):
                if nxt in dead or nxt in visited:
                    continue
                if nxt == target:
                    return dist + 1
                visited.add(nxt)
                q.append((nxt, dist + 1))
        return -1
