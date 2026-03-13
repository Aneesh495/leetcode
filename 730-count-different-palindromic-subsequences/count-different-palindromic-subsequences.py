
class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MOD = 1_000_000_007
        n = len(s)
        if n == 0:
            return 0

        prev_occ = [-1] * n
        last = {}
        for i, ch in enumerate(s):
            prev_occ[i] = last.get(ch, -1)
            last[ch] = i

        next_occ = [n] * n
        next_seen = {}
        for i in range(n - 1, -1, -1):
            ch = s[i]
            next_occ[i] = next_seen.get(ch, n)
            next_seen[ch] = i

        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    low = next_occ[i]
                    high = prev_occ[j]
                    if low > high:
                        dp[i][j] = (2 * dp[i + 1][j - 1] + 2) % MOD
                    elif low == high:
                        dp[i][j] = (2 * dp[i + 1][j - 1] + 1) % MOD
                    else:
                        dp[i][j] = (2 * dp[i + 1][j - 1] - dp[low + 1][high - 1]) % MOD
                else:
                    dp[i][j] = (dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]) % MOD

        return dp[0][n - 1] % MOD
