
from typing import List

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res = set()
        cur = set()
        for a in arr:
            nxt = {a}
            for v in cur:
                nxt.add(v | a)
            res.update(nxt)
            cur = nxt
        return len(res)
