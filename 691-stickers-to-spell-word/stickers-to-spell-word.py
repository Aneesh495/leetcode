
from typing import List
from functools import lru_cache

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        m = len(stickers)
        cnt = [[0]*26 for _ in range(m)]
        for i, s in enumerate(stickers):
            for ch in s:
                cnt[i][ord(ch) - 97] += 1

        @lru_cache(None)
        def dfs(rem: str) -> int:
            if not rem:
                return 0
            need = [0]*26
            for ch in rem:
                need[ord(ch) - 97] += 1
            res = float('inf')
            first = ord(rem[0]) - 97
            for c in cnt:
                if c[first] == 0:
                    continue
                new_rem = []
                for i in range(26):
                    if need[i] > 0:
                        left = need[i] - c[i]
                        if left > 0:
                            new_rem.extend(chr(i + 97) * left)
                nxt = ''.join(new_rem)
                t = dfs(nxt)
                if t != -1:
                    res = min(res, 1 + t)
            return -1 if res == float('inf') else res

        return dfs(''.join(sorted(target)))
