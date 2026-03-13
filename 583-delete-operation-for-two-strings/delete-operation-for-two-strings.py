
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # compute LCS length with 1D DP
        if not word1 or not word2:
            return len(word1) + len(word2)
        if len(word2) > len(word1):
            word1, word2 = word2, word1
        m, n = len(word1), len(word2)
        dp = [0] * (n + 1)
        for i in range(1, m + 1):
            prev = 0
            a = word1[i - 1]
            for j in range(1, n + 1):
                temp = dp[j]
                if a == word2[j - 1]:
                    dp[j] = prev + 1
                else:
                    dp[j] = dp[j] if dp[j] >= dp[j - 1] else dp[j - 1]
                prev = temp
        lcs = dp[n]
        return m + n - 2 * lcs
