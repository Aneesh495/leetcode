
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Two pointer sweep
        # Left starts at index 0
        # Right starts at last index
        # The area is width multiplied by the shorter wall
        # Move the pointer at the shorter wall inward since only that can raise the min height
        # Track the best area seen

        left = 0
        right = len(height) - 1
        best = 0

        while left < right:
            # Compute current area
            h = height[left] if height[left] < height[right] else height[right]
            width = right - left
            area = h * width
            if area > best:
                best = area

            # Move the limiting wall inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return best