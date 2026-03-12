
from typing import List

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        # Greedy
        # Maintain smallest sum in [1, miss) that is currently coverable
        # If next array value <= miss we extend coverage by that value
        # Otherwise patch with miss itself which doubles coverage
        miss = 1
        i = 0
        patches = 0
        length = len(nums)

        while miss <= n:
            if i < length and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                patches += 1
        return patches
