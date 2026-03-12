
from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        O(n) time and O(1) space
        Keep the smallest value seen so far and the smallest second value for a valid pair
        If we find a number larger than both we have an increasing triplet
        """
        first = float("inf")   # smallest number so far
        second = float("inf")  # smallest possible middle number greater than first

        for x in nums:
            if x <= first:
                # new smallest
                first = x
            elif x <= second:
                # x is greater than first and can serve as a better second
                second = x
            else:
                # x is greater than both first and second
                return True

        return False
