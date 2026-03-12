
from typing import List

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # Scan from right to left
        # third stores the best candidate for nums[k]
        # Stack stores decreasing candidates for nums[j]
        third = float("-inf")
        stack: List[int] = []
        for x in reversed(nums):
            # If we find nums[i] less than third then 132 exists
            if x < third:
                return True
            # While x can be nums[j] pop smaller items into third
            while stack and x > stack[-1]:
                third = stack.pop()
            # Push x as a new candidate for nums[j]
            stack.append(x)
        return False
