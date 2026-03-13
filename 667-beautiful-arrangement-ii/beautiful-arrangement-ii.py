
from typing import List

class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        res = []
        l, r = 1, k + 1
        while l <= r:
            res.append(l)
            l += 1
            if l <= r:
                res.append(r)
                r -= 1
        for x in range(k + 2, n + 1):
            res.append(x)
        return res
