
from typing import List
from functools import lru_cache

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        # Returns True if player 1 can achieve a non-negative score difference
        # against an optimal opponent by playing optimally themself.
        @lru_cache(None)
        def best_diff(l: int, r: int) -> int:
            # Best score difference current player can secure from nums[l:r+1]
            if l == r:
                return nums[l]
            take_left = nums[l] - best_diff(l + 1, r)
            take_right = nums[r] - best_diff(l, r - 1)
            return max(take_left, take_right)

        return best_diff(0, len(nums) - 1) >= 0
