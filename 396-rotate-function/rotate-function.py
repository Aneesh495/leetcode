
from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        # n is the length of nums
        n = len(nums)
        # total is the sum of all elements in nums
        total = sum(nums)
        # f0 is F(0) which equals sum(i * nums[i]) for i from 0 to n - 1
        f0 = sum(i * v for i, v in enumerate(nums))
        # ans tracks the maximum F(k) seen so far
        ans = f0
        # fk holds the current F(k) while iterating k from 1 to n - 1
        fk = f0
        # Use the recurrence
        # F(k) = F(k - 1) + total - n * nums[n - k]
        for k in range(1, n):
            fk = fk + total - n * nums[-k]
            if fk > ans:
                ans = fk
        return ans
