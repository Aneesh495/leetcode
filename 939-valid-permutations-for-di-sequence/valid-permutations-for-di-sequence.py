
class Solution:
    def numPermsDISequence(self, s: str) -> int:
        MOD = 10**9 + 7
        dp = [1]
        for ch in s:
            n = len(dp)
            ndp = [0] * (n + 1)
            if ch == 'I':
                run = 0
                for j in range(1, n + 1):
                    run = (run + dp[j - 1]) % MOD
                    ndp[j] = run
            else:
                run = 0
                for j in range(n - 1, -1, -1):
                    run = (run + dp[j]) % MOD
                    ndp[j] = run
            dp = ndp
        return sum(dp) % MOD
