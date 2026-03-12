
from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """
        0 1 knapsack on two capacities
        dp[i][j] stores the max subset size using at most i zeros and j ones
        iterate capacities in reverse to ensure each string is used at most once
        """
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            zeros = s.count('0')                  # cost in zeros
            ones = len(s) - zeros                # cost in ones

            for i in range(m, zeros - 1, -1):    # reverse to avoid reuse
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)

        return dp[m][n]
