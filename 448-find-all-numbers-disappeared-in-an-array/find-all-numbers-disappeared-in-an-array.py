
from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Mark seen numbers by negating the value at their mapped index
        # Each value v is in 1..n so map to index v-1
        for v in nums:
            i = abs(v) - 1
            if nums[i] > 0:
                nums[i] = -nums[i]

        # Indices that remain positive were never marked
        # Those indices correspond to missing values i+1
        return [i + 1 for i, val in enumerate(nums) if val > 0]
