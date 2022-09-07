from functools import lru_cache
from math import gcd

class Solution:
    def maxScore(self, nums: list[int]) -> int:
        n = len(nums)
        full = (1 << n) - 1

        @lru_cache(None)
        def dp(mask: int) -> int:
            if mask == full:
                return 0
            operation = mask.bit_count() // 2 + 1
            best = 0
            for i in range(n):
                if mask & (1 << i):
                    continue
                for j in range(i + 1, n):
                    if mask & (1 << j):
                        continue
                    next_mask = mask | (1 << i) | (1 << j)
                    best = max(best, operation * gcd(nums[i], nums[j]) + dp(next_mask))
            return best

        return dp(0)