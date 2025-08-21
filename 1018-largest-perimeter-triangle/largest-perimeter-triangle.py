
from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # Sort sides in descending order so the first valid triple gives max perimeter
        nums.sort(reverse=True)
        # Check consecutive triples. For sides a ≥ b ≥ c a triangle exists if b + c > a
        for i in range(len(nums) - 2):
            a, b, c = nums[i], nums[i + 1], nums[i + 2]
            if b + c > a:
                return a + b + c
        # No valid triangle found
        return 0
