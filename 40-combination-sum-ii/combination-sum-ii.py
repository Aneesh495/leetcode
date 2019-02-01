
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sort so we can prune early and skip duplicates cleanly
        candidates.sort()
        res: List[List[int]] = []
        path: List[int] = []

        def dfs(start: int, remain: int) -> None:
            # If we hit target record current path
            if remain == 0:
                res.append(path.copy())
                return
            # Walk choices from current start
            prev = None  # tracks the last value used at this depth to skip duplicates
            for i in range(start, len(candidates)):
                val = candidates[i]
                # Skip duplicates at the same tree depth
                if prev is not None and val == prev:
                    continue
                # Prune since remaining target will only get smaller from here
                if val > remain:
                    break
                path.append(val)
                dfs(i + 1, remain - val)  # i + 1 because each number can be used once
                path.pop()
                prev = val  # mark this value as used at this depth

        dfs(0, target)
        return res
