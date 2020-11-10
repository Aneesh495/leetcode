
from typing import List

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        moves = 0
        next_free = -10**20
        for x in nums:
            if x <= next_free:
                moves += next_free + 1 - x
                next_free += 1
            else:
                next_free = x
        return moves
