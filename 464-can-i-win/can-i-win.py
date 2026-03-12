
from functools import lru_cache

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # Quick outcomes
        if desiredTotal <= 0:
            return True
        total_sum = maxChoosableInteger * (maxChoosableInteger + 1) // 2
        if total_sum < desiredTotal:
            return False

        # Use bitmask to represent used numbers
        # mask bit i means number i used where i runs 1..maxChoosableInteger and stored at bit i
        @lru_cache(None)
        def dfs(mask: int, need: int) -> bool:
            # Current player wins if there exists a choice i not used
            # such that i reaches or exceeds need or it forces opponent loss
            for i in range(1, maxChoosableInteger + 1):
                bit = 1 << i
                if mask & bit:
                    continue
                if i >= need:
                    return True
                if not dfs(mask | bit, need - i):
                    return True
            return False

        return dfs(0, desiredTotal)
