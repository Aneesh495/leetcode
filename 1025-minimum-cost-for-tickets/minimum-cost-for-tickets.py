
from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # dp[i] is the minimum cost to cover all travel up to day i
        last = days[-1]
        travel = set(days)
        dp = [0] * (last + 1)

        c1, c7, c30 = costs
        for d in range(1, last + 1):
            if d not in travel:
                dp[d] = dp[d - 1]
            else:
                cost1 = dp[d - 1] + c1
                cost7 = dp[max(0, d - 7)] + c7
                cost30 = dp[max(0, d - 30)] + c30
                dp[d] = min(cost1, cost7, cost30)
        return dp[last]
