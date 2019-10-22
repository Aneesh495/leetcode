
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s & 1:
            return False
        target = s // 2
        bits = 1
        for x in nums:
            bits |= bits << x
            if (bits >> target) & 1:
                return True
        return False
