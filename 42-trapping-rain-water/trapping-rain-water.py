
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 2:
            return 0

        l, r = 0, n - 1                 # pointers at both ends
        left_max, right_max = 0, 0      # best walls seen so far
        water = 0

        while l < r:
            if height[l] <= height[r]:
                # left side is the limiting wall
                if height[l] >= left_max:
                    left_max = height[l]  # update best left wall
                else:
                    water += left_max - height[l]  # trap above current left bar
                l += 1
            else:
                # right side is the limiting wall
                if height[r] >= right_max:
                    right_max = height[r]  # update best right wall
                else:
                    water += right_max - height[r]  # trap above current right bar
                r -= 1

        return water
