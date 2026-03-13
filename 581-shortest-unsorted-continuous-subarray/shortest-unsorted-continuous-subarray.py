
from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        right = -1
        left = n
        max_so_far = nums[0]
        for i in range(1, n):
            if nums[i] < max_so_far:
                right = i
            else:
                max_so_far = nums[i]
        if right == -1:
            return 0
        min_so_far = nums[-1]
        for i in range(n - 2, -1, -1):
            if nums[i] > min_so_far:
                left = i
            else:
                min_so_far = nums[i]
        return right - left + 1
