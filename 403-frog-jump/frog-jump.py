
from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # Early pruning. If any gap is bigger than the max possible step at that index then fail
        # Because the earliest you can reach index i is with at most step size i
        for i in range(1, len(stones)):
            if stones[i] - stones[i - 1] > i:
                return False

        # Map stone position to its index for O(1) lookups
        pos_to_idx = {pos: i for i, pos in enumerate(stones)}
        last_pos = stones[-1]

        # Memo for DFS. Key is (index, last_jump). Value is bool
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dfs(i: int, k: int) -> bool:
            # If we are at the last stone then success
            if stones[i] == last_pos:
                return True

            # Try next jumps k-1 k k+1. Ignore nonpositive jumps
            for step in (k - 1, k, k + 1):
                if step <= 0:
                    continue
                next_pos = stones[i] + step
                # If there is a stone at next_pos then continue search
                j = pos_to_idx.get(next_pos)
                if j is not None and dfs(j, step):
                    return True
            return False

        # First jump must be 1 and the second stone must be at position 1
        if len(stones) < 2 or stones[1] != 1:
            return False

        return dfs(1, 1)
