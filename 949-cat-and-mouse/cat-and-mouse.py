
from collections import deque
from typing import List

class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)
        DRAW, MOUSE, CAT = 0, 1, 2

        color = [[[DRAW] * 3 for _ in range(n)] for _ in range(n)]
        degree = [[[0] * 3 for _ in range(n)] for _ in range(n)]

        for m in range(n):
            for c in range(n):
                degree[m][c][MOUSE] = len(graph[m])
                degree[m][c][CAT] = sum(1 for nxt in graph[c] if nxt != 0)

        q = deque()

        for c in range(n):
            for t in (MOUSE, CAT):
                if color[0][c][t] == DRAW:
                    color[0][c][t] = MOUSE
                    q.append((0, c, t, MOUSE))

        for m in range(n):
            for t in (MOUSE, CAT):
                if color[m][m][t] == DRAW:
                    color[m][m][t] = CAT
                    q.append((m, m, t, CAT))

        def parents(m: int, c: int, t: int):
            if t == MOUSE:
                for pc in graph[c]:
                    if pc == 0:
                        continue
                    yield (m, pc, CAT)
            else:
                for pm in graph[m]:
                    yield (pm, c, MOUSE)

        while q:
            m, c, t, res = q.popleft()
            for pm, pc, pt in parents(m, c, t):
                if color[pm][pc][pt] != DRAW:
                    continue
                if pt == res:
                    color[pm][pc][pt] = res
                    q.append((pm, pc, pt, res))
                else:
                    degree[pm][pc][pt] -= 1
                    if degree[pm][pc][pt] == 0:
                        opp = CAT if pt == MOUSE else MOUSE
                        color[pm][pc][pt] = opp
                        q.append((pm, pc, pt, opp))

        return color[1][2][MOUSE]
