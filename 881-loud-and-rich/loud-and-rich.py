
from typing import List
import sys
sys.setrecursionlimit(1 << 25)

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        g = [[] for _ in range(n)]  # g[v]: people richer than v
        for u, v in richer:
            g[v].append(u)

        ans = [-1] * n

        def dfs(i: int) -> int:
            if ans[i] != -1:
                return ans[i]
            best = i
            for u in g[i]:
                cand = dfs(u)
                if quiet[cand] < quiet[best]:
                    best = cand
            ans[i] = best
            return best

        for i in range(n):
            dfs(i)
        return ans
