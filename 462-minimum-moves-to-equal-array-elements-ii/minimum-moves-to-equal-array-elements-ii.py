
from typing import List

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # Sort to pair smallest with largest
        nums.sort()
        l, r = 0, len(nums) - 1
        moves = 0
        # Each pair contributes difference toward the median
        while l < r:
            moves += nums[r] - nums[l]
            l += 1
            r -= 1
        return moves
