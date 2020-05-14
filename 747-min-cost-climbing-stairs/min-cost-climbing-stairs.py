
from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev2 = prev1 = 0
        for c in cost:
            curr = min(prev1, prev2) + c
            prev2, prev1 = prev1, curr
        return min(prev1, prev2)
