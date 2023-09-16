
from typing import List
from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # dp[i] maps a difference to the count of subsequences ending at i with length at least 2
        dp = [defaultdict(int) for _ in nums]
        res = 0

        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]  # Python int is unbounded so this is safe
                cnt = dp[j][diff]         # subsequences ending at j that we can extend
                res += cnt                # each such subsequence becomes length at least 3
                dp[i][diff] += cnt + 1    # add pairs (j,i) and all extended ones

        return res
