
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        Bottom up DP
        dp[i][j] stores the length of the longest palindromic subsequence in s[i..j]
        Transition
          if s[i] == s[j] then dp[i][j] = dp[i + 1][j - 1] + 2
          else dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        Answer is dp[0][n - 1]
        Time O(n^2)  Space O(n^2)
        """
        n = len(s)
        if n <= 1:
            return n

        dp = [[0] * n for _ in range(n)]

        # substrings of length 1 are palindromes of length 1
        for i in range(n):
            dp[i][i] = 1

        # build for increasing lengths
        for length in range(2, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]
