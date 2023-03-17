
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything modify nums in place
        Stable relative order of non zero elements
        One pass two pointer swap
        """
        last = 0  # index of next spot to place a non zero
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last], nums[i] = nums[i], nums[last]
                last += 1
