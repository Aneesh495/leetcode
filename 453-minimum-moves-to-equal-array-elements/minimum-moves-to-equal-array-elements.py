
from typing import List

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # Each move increments n minus 1 elements by 1
        # This is equivalent to decrementing one element by 1 per move
        # Bring all elements down to the minimum
        # Moves equal sum of elements minus minimum times count
        m = min(nums)
        return sum(nums) - m * len(nums)
