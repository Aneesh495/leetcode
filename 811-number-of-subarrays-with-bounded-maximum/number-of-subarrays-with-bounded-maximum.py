
from typing import List

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def count_at_most(bound: int) -> int:
            res = 0
            cur = 0
            for x in nums:
                if x <= bound:
                    cur += 1
                else:
                    cur = 0
                res += cur
            return res

        return count_at_most(right) - count_at_most(left - 1)
