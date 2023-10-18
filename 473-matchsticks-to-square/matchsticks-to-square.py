
from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # A square needs total length divisible by 4
        total = sum(matchsticks)
        if total % 4 != 0 or len(matchsticks) < 4:
            return False

        target = total // 4

        # Place longer sticks first to prune faster
        matchsticks.sort(reverse=True)
        if matchsticks[0] > target:
            return False

        sides = [0, 0, 0, 0]

        def dfs(i: int) -> bool:
            # All sticks placed
            if i == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == sides[3] == target

            v = matchsticks[i]

            # Try to place current stick on each side
            for k in range(4):
                if sides[k] + v <= target:
                    sides[k] += v
                    if dfs(i + 1):
                        return True
                    sides[k] -= v

                # Symmetry pruning when a side is still empty
                if sides[k] == 0:
                    break

            return False

        return dfs(0)
