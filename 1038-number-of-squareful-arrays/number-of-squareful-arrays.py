
from typing import List
from functools import lru_cache
import math

class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        # Sort to enable duplicate-skipping logic
        nums.sort()
        n = len(nums)

        # Precompute adjacency: edges between indices whose values sum to a perfect square
        def is_square(x: int) -> bool:
            r = int(math.isqrt(x))
            return r * r == x

        adj = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j and is_square(nums[i] + nums[j]):
                    adj[i].append(j)

        @lru_cache(None)
        def dfs(mask: int, last: int) -> int:
            if mask == (1 << n) - 1:
                return 1
            total = 0
            prev_val = None  # duplicate control at this depth
            for j in adj[last]:
                if mask & (1 << j):
                    continue
                # Skip using the same value twice at the same decision level
                if prev_val is not None and nums[j] == prev_val:
                    continue
                # Classic duplicate rule for permutations with indices:
                # if an identical previous index is unused, skip current to avoid reordering duplicates
                if j > 0 and nums[j] == nums[j - 1] and not (mask & (1 << (j - 1))):
                    continue
                total += dfs(mask | (1 << j), j)
                prev_val = nums[j]
            return total

        # Start from each index. Apply starting-duplicate rule.
        ans = 0
        used_starts = set()
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            ans += dfs(1 << i, i)
        return ans
