
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Write non val elements to the front
        # Maintain k as the next write position
        k = 0
        for x in nums:
            if x != val:
                nums[k] = x
                k += 1
        # First k positions hold the kept elements
        return k
