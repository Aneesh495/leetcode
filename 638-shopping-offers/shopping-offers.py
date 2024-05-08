
from functools import lru_cache
from typing import List

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(price)

        # prune specials that are never better than buying items individually
        pruned = []
        for sp in special:
            cost_items = sum(sp[i] * price[i] for i in range(n))
            if cost_items > sp[-1] and any(sp[i] > 0 for i in range(n)):
                pruned.append(sp)

        @lru_cache(None)
        def dfs(state: tuple) -> int:
            # cost without specials
            best = sum(state[i] * price[i] for i in range(n))
            # try each special if applicable
            for sp in pruned:
                nxt = []
                ok = True
                for i in range(n):
                    if sp[i] > state[i]:
                        ok = False
                        break
                    nxt.append(state[i] - sp[i])
                if ok:
                    best = min(best, sp[-1] + dfs(tuple(nxt)))
            return best

        return dfs(tuple(needs))
