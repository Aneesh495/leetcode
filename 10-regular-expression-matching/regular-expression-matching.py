class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dp[i][j] means s[:i] matches p[:j]
        m = len(s)
        n = len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        # empty s with pattern prefixes like a* or a*b* or .* etc
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        def matches(i: int, j: int) -> bool:
            if i == 0:
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]

        for i in range(0, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] != '*':
                    if matches(i, j):
                        dp[i][j] = dp[i - 1][j - 1]
                else:
                    # star uses zero of the previous element
                    dp[i][j] = dp[i][j - 2]
                    # star uses one or more of the previous element
                    if i > 0 and (p[j - 2] == '.' or p[j - 2] == s[i - 1]):
                        dp[i][j] = dp[i][j] or dp[i - 1][j]

        return dp[m][n]