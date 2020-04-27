
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        total = sum(map(ord, s1)) + sum(map(ord, s2))
        dp = [0] * (n + 1)
        for i in range(1, m + 1):
            prev = 0
            for j in range(1, n + 1):
                temp = dp[j]
                if s1[i - 1] == s2[j - 1]:
                    dp[j] = prev + ord(s1[i - 1])
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                prev = temp
        return total - 2 * dp[n]
