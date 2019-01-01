from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Map each value to its earliest index
        seen = {}
        # Walk through the array once
        for i, x in enumerate(nums):
            need = target - x               # The partner value we are looking for
            if need in seen:               # If we have seen the partner already we are done
                return [seen[need], i]
            # Store current value with its index for future lookups
            seen[x] = i
        # Problem guarantees exactly one solution
        return []