
from functools import lru_cache
from typing import List

class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        """
        LeetCode 1000. Minimum Cost to Merge Stones
        Interval DP with (k-1)-step partitioning.
        dp(i, j) = minimum cost to merge stones[i..j] into 1 pile
        We only add the segment sum when the length allows merging to 1 pile:
            (j - i) % (k - 1) == 0
        Otherwise we can only merge to more than 1 pile and must keep splitting.
        Splits jump by (k - 1) to ensure the number of piles reduces correctly.
        """
        n = len(stones)

        # If total piles cannot be reduced to 1 by repeatedly merging k piles, impossible
        if (n - 1) % (k - 1) != 0:
            return -1

        # Prefix sums for O(1) range sum
        prefix = [0]
        for x in stones:
            prefix.append(prefix[-1] + x)

        def range_sum(i: int, j: int) -> int:
            return prefix[j + 1] - prefix[i]

        @lru_cache(None)
        def dp(i: int, j: int) -> int:
            # Cost to merge stones[i..j] into one pile
            if i == j:
                return 0

            INF = 10 ** 18
            res = INF

            # Try splitting at m with step (k - 1)
            # This preserves the invariant on piles count
            m = i
            while m < j:
                res = min(res, dp(i, m) + dp(m + 1, j))
                m += k - 1

            # If length allows merging the resulting k piles into one, add sum
            if (j - i) % (k - 1) == 0:
                res += range_sum(i, j)

            return res

        return dp(0, n - 1)
