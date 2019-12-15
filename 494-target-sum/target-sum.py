
from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        if abs(target) > s:
            return 0
        if (s + target) % 2 != 0:
            return 0
        P = (s + target) // 2
        dp = [0] * (P + 1)
        dp[0] = 1
        for x in nums:
            for t in range(P, x - 1, -1):
                dp[t] += dp[t - x]
        return dp[P]
