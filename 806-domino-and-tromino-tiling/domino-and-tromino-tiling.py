
class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp0, dp1, dp2 = 1, 1, 2  # dp[i-3], dp[i-2], dp[i-1]
        for i in range(3, n + 1):
            dp3 = (2 * dp2 + dp0) % MOD
            dp0, dp1, dp2 = dp1, dp2, dp3
        return dp2
