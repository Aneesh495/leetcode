
class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, goal + 1):
            ndp = [0] * (n + 1)
            up = min(i, n)
            for j in range(1, up + 1):
                add_new = dp[j - 1] * (n - (j - 1))
                add_old = dp[j] * max(j - k, 0)
                ndp[j] = (add_new + add_old) % MOD
            dp = ndp
        return dp[n] % MOD
