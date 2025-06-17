
from typing import List

class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        s, t = list(stamp), list(target)
        m, n = len(s), len(t)
        res = []
        visited = [False] * (n - m + 1)
        stars = 0

        def can_stamp(i):
            made_change = False
            for j in range(m):
                if t[i + j] == '?':
                    continue
                if t[i + j] != s[j]:
                    return False
                made_change = True
            return made_change

        def do_stamp(i):
            nonlocal stars
            for j in range(m):
                if t[i + j] != '?':
                    t[i + j] = '?'
                    stars += 1

        while stars < n:
            changed = False
            for i in range(n - m + 1):
                if not visited[i] and can_stamp(i):
                    do_stamp(i)
                    visited[i] = True
                    changed = True
                    res.append(i)
                    if stars == n:
                        break
            if not changed:
                return []
        return res[::-1]
