
from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        if not nums:
            return res

        start = prev = nums[0]

        for x in nums[1:]:
            if x == prev + 1:
                prev = x
                continue
            res.append(str(start) if start == prev else f"{start}->{prev}")
            start = prev = x

        res.append(str(start) if start == prev else f"{start}->{prev}")
        return res
