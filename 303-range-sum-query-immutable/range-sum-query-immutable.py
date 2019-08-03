
from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        # Build prefix sums where pref[i] stores sum of nums[0..i-1]
        self.pref = [0]
        for x in nums:
            self.pref.append(self.pref[-1] + x)

    def sumRange(self, left: int, right: int) -> int:
        # Sum of nums[left..right] equals pref[right+1] - pref[left]
        return self.pref[right + 1] - self.pref[left]
