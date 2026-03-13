
from typing import List

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        max1 = -1
        max2 = -1
        idx = -1
        for i, v in enumerate(nums):
            if v > max1:
                max2 = max1
                max1 = v
                idx = i
            elif v > max2:
                max2 = v
        return idx if max1 >= 2 * max2 else -1
