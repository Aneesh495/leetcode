
from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # Use indices as buckets by marking seen numbers negative in place
        # If we hit an index already negative the number is a duplicate
        res: List[int] = []
        for v in nums:
            i = abs(v) - 1
            if nums[i] < 0:
                res.append(i + 1)
            else:
                nums[i] = -nums[i]
        return res
