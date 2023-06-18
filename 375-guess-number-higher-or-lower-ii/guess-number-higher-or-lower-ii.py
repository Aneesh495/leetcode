
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # dp[l][r] stores the minimum money needed to guarantee a win for the range [l, r]
        # dp[l][r] = min over x in [l, r] of x + max(dp[l][x - 1], dp[x + 1][r])
        # When l >= r the cost is zero because there is at most one number to guess
        
        INF = 10**9
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        
        # length is the current interval size
        for length in range(2, n + 1):
            for l in range(1, n - length + 2):
                r = l + length - 1
                best = INF
                # try each pivot x in [l, r]
                for x in range(l, r + 1):
                    left = dp[l][x - 1]
                    right = dp[x + 1][r]
                    cost = x + max(left, right)
                    if cost < best:
                        best = cost
                dp[l][r] = best
        
        return dp[1][n]
