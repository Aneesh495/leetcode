
from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Track the top three distinct values seen so far
        first = second = third = None

        for x in nums:
            # Skip duplicates so only distinct values count
            if x == first or x == second or x == third:
                continue

            # Insert x into the correct slot among first second third
            if first is None or x > first:
                third = second
                second = first
                first = x
            elif second is None or x > second:
                third = second
                second = x
            elif third is None or x > third:
                third = x

        # If there are at least three distinct values return the third
        # Otherwise return the maximum which is stored in first
        return third if third is not None else first
