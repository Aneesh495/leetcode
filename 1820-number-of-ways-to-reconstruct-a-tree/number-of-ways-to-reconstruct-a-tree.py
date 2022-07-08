from collections import defaultdict
class Solution:
    def checkWays(self, pairs):
        g=defaultdict(set)
        for a,b in pairs: g[a].add(b); g[b].add(a)
        n=len(g); roots=[v for v in g if len(g[v])==n-1]
        if not roots: return 0
        root=roots[0]; ans=1
        for v in g:
            if v==root: continue
            d=len(g[v]); candidates=[u for u in g[v] if len(g[u])>=d]
            if not candidates: return 0
            p=min(candidates,key=lambda u:len(g[u]))
            if not (g[v]-{p})<=g[p]: return 0
            if len(g[p])==d: ans=2
        return ans