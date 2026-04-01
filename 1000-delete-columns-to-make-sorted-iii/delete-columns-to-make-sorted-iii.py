
from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        """
        LeetCode 960 Delete Columns to Make Sorted III
        Keep the largest set of columns that is nondecreasing in every row
        Answer is total columns minus size of this set
        Use DP like Longest Nondecreasing Subsequence over columns
        Two columns i and j are compatible if for every row r we have strs[r][i] <= strs[r][j]
        """
        if not strs:
            return 0

        n = len(strs)            # number of rows
        m = len(strs[0])         # number of columns

        # dp[j] is the longest valid length that ends at column j
        dp = [1] * m

        # For each pair of columns i < j check if i can come before j
        for j in range(m):
            for i in range(j):
                ok = True
                # Check compatibility across all rows
                for r in range(n):
                    if strs[r][i] > strs[r][j]:
                        ok = False
                        break
                if ok:
                    dp[j] = max(dp[j], dp[i] + 1)

        longest_keep = max(dp)
        return m - longest_keep
