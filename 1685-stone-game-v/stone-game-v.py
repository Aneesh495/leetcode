from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        prefix = [0] * (n + 1)
        for i, value in enumerate(stoneValue):
            prefix[i + 1] = prefix[i] + value

        dp = [[0] * n for _ in range(n)]
        left_best = [[-10**18] * n for _ in range(n)]
        right_best = [[0] * n for _ in range(n)]
        for i in range(n):
            right_best[i][i] = -prefix[i]

        for j in range(1, n):
            for i in range(j - 1, -1, -1):
                best = dp[i][j - 1] + prefix[j]
                if j - 1 > i:
                    best = max(best, left_best[i][j - 1])
                left_best[i][j] = best

                total = prefix[i] + prefix[j + 1]
                value = 0

                left_end = bisect_right(prefix, (total - 1) // 2, i + 1, j + 1)
                if left_end > i + 1:
                    value = max(value, left_best[i][left_end - 1] - prefix[i])

                right_start = bisect_right(prefix, total // 2, i + 1, j + 1)
                if right_start <= j:
                    value = max(value, prefix[j + 1] + right_best[right_start][j])

                if total % 2 == 0:
                    split = bisect_left(prefix, total // 2, i + 1, j + 1)
                    if split <= j and 2 * prefix[split] == total:
                        value = max(value, prefix[split] - prefix[i] + max(dp[i][split - 1], dp[split][j]))

                dp[i][j] = value
                right_best[i][j] = max(dp[i][j] - prefix[i], right_best[i + 1][j])

        return dp[0][n - 1]