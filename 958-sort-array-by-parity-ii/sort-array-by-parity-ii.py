
from typing import List

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i, j = 0, 1
        while i < n and j < n:
            if nums[i] % 2 == 0:
                i += 2
                continue
            if nums[j] % 2 == 1:
                j += 2
                continue
            nums[i], nums[j] = nums[j], nums[i]
            i += 2
            j += 2
        return nums
