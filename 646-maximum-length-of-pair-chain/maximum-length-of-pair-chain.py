
from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        res = 0
        cur = float('-inf')
        for a, b in pairs:
            if a > cur:
                res += 1
                cur = b
        return res
