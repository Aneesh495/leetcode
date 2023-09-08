
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m = len(p)
        if m > n:
            return []
        cnt = [0] * 26
        for c in p:
            cnt[ord(c) - 97] += 1
        for i in range(m):
            cnt[ord(s[i]) - 97] -= 1
        def all_zero():
            for x in cnt:
                if x != 0:
                    return False
            return True
        res = []
        if all_zero():
            res.append(0)
        for i in range(m, n):
            cnt[ord(s[i]) - 97] -= 1
            cnt[ord(s[i - m]) - 97] += 1
            if all_zero():
                res.append(i - m + 1)
        return res
