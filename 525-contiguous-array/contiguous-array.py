
from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first_index = {0: -1}
        prefix = 0
        best = 0
        for i, v in enumerate(nums):
            prefix += 1 if v == 1 else -1
            if prefix in first_index:
                best = max(best, i - first_index[prefix])
            else:
                first_index[prefix] = i
        return best
