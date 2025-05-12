
from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)
        cur_max = max_so_far = nums[0]
        cur_min = min_so_far = nums[0]
        for x in nums[1:]:
            cur_max = max(x, cur_max + x)
            max_so_far = max(max_so_far, cur_max)
            cur_min = min(x, cur_min + x)
            min_so_far = min(min_so_far, cur_min)
        if max_so_far < 0:
            return max_so_far
        return max(max_so_far, total - min_so_far)
