
from typing import List

class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        n = len(nums)
        if n == 1:
            return str(nums[0])
        if n == 2:
            return f"{nums[0]}/{nums[1]}"
        middle = "/".join(str(x) for x in nums[1:])
        return f"{nums[0]}/({middle})"
