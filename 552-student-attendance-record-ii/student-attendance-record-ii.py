
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        # dp[a][l] where
        # a is number of A used so far. It is 0 or 1
        # l is current consecutive L count. It is 0 to 2
        dp = [[0, 0, 0], [0, 0, 0]]
        dp[0][0] = 1  # empty sequence

        for _ in range(n):
            ndp = [[0, 0, 0], [0, 0, 0]]

            # Add 'P' resets late streak
            for a in (0, 1):
                total = (dp[a][0] + dp[a][1] + dp[a][2]) % MOD
                ndp[a][0] = (ndp[a][0] + total) % MOD

            # Add 'A' only if we have not used any A yet
            total_noA = (dp[0][0] + dp[0][1] + dp[0][2]) % MOD
            ndp[1][0] = (ndp[1][0] + total_noA) % MOD

            # Add 'L' increases late streak by one up to two
            for a in (0, 1):
                ndp[a][1] = (ndp[a][1] + dp[a][0]) % MOD
                ndp[a][2] = (ndp[a][2] + dp[a][1]) % MOD

            dp = ndp

        ans = 0
        for a in (0, 1):
            for l in range(3):
                ans = (ans + dp[a][l]) % MOD
        return ans
