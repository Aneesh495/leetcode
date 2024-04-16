class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        MOD = 10**9 + 7
        m = target // 2
        if n <= m:
            return (n * (n + 1) // 2) % MOD
        rem = n - m
        return (m * (m + 1) // 2 + rem * target + rem * (rem - 1) // 2) % MOD
