
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        banned = {tuple(m) for m in mines}
        dp = [[n] * n for _ in range(n)]

        # Left
        for i in range(n):
            run = 0
            for j in range(n):
                run = 0 if (i, j) in banned else run + 1
                dp[i][j] = min(dp[i][j], run)
            run = 0
            for j in range(n - 1, -1, -1):
                run = 0 if (i, j) in banned else run + 1
                dp[i][j] = min(dp[i][j], run)

        ans = 0
        # Up and Down
        for j in range(n):
            run = 0
            for i in range(n):
                run = 0 if (i, j) in banned else run + 1
                dp[i][j] = min(dp[i][j], run)
            run = 0
            for i in range(n - 1, -1, -1):
                run = 0 if (i, j) in banned else run + 1
                dp[i][j] = min(dp[i][j], run)
                ans = max(ans, dp[i][j])

        return ans
