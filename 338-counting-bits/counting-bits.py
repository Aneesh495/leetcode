
from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        # res[i] will hold the number of set bits in i
        res = [0] * (n + 1)
        # Use the relation bits(i) = bits(i >> 1) + (i & 1)
        # i >> 1 removes the least significant bit
        # i & 1 is 1 if i is odd else 0
        for i in range(1, n + 1):
            res[i] = res[i >> 1] + (i & 1)
        return res
