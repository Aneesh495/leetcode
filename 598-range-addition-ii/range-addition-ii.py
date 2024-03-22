
from typing import List

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m * n
        min_a = min(a for a, _ in ops)
        min_b = min(b for _, b in ops)
        return min_a * min_b
