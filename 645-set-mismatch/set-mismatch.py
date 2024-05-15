
from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = set(nums)
        dup = sum(nums) - sum(s)
        missing = len(nums) * (len(nums) + 1) // 2 - sum(s)
        return [dup, missing]
