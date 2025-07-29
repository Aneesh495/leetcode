
from typing import List

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        # Monotonic decreasing stack of indices for left candidates
        stack: List[int] = []
        for i, v in enumerate(nums):
            if not stack or v < nums[stack[-1]]:
                stack.append(i)

        ans = 0
        # Scan from right to left and pop while we can form a ramp
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[j] >= nums[stack[-1]]:
                ans = max(ans, j - stack[-1])
                stack.pop()
            if j <= ans:
                break
        return ans
