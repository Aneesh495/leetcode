
from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # Dynamic programming
        # dp[j] stores the size of the largest all 1s square
        # whose bottom right corner is at current row i and column j
        # We use rolling 1D array to reduce space to O(n)
        # Transition for cell with value 1
        # dp[j] = 1 + min(prev, dp[j], dp[j-1])
        # where
        # prev is dp[j-1] from previous row which represents top left neighbor
        # dp[j] before update is top neighbor
        # dp[j-1] after update is left neighbor
        if not matrix or not matrix[0]:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        dp = [0] * (cols + 1)  # extra leading zero simplifies boundary checks
        max_side = 0

        for i in range(1, rows + 1):
            prev = 0  # this holds dp[j-1] from previous row which is top left neighbor
            for j in range(1, cols + 1):
                temp = dp[j]  # save top neighbor before we overwrite it
                if matrix[i - 1][j - 1] == '1':
                    # dp[j] currently is top
                    # dp[j-1] currently is left
                    # prev currently is top left
                    dp[j] = 1 + min(prev, dp[j], dp[j - 1])
                    if dp[j] > max_side:
                        max_side = dp[j]
                else:
                    dp[j] = 0
                prev = temp  # move window for next column
        return max_side * max_side
