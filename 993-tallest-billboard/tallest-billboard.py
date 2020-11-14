
from typing import List
from collections import defaultdict

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        """
        Dynamic programming by difference of two sides
        dp[diff] stores the best possible taller side height for this diff
        diff equals taller minus shorter and is always non negative
        Answer is dp[0] which means both sides can be made equal
        """
        NEG = -10**9
        dp = defaultdict(lambda: NEG)
        dp[0] = 0

        for r in rods:
            prev = dict(dp)  # snapshot to avoid double use of the same rod
            for diff, tall in prev.items():
                # Option 1 skip this rod
                if tall > dp[diff]:
                    dp[diff] = tall

                # Option 2 add rod to the taller side
                # Taller side height increases by r and diff grows by r
                ndiff = diff + r
                ntall = tall + r
                if ntall > dp[ndiff]:
                    dp[ndiff] = ntall

                # Option 3 add rod to the shorter side
                # New difference is abs(diff minus r)
                # New taller height increases only if r is larger than diff
                ndiff = abs(diff - r)
                ntall = tall + max(0, r - diff)
                if ntall > dp[ndiff]:
                    dp[ndiff] = ntall

        return dp[0]
