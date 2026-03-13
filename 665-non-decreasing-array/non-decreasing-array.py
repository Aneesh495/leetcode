
from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        changed = 0
        for i in range(len(nums) - 1):
            if nums[i] <= nums[i + 1]:
                continue
            changed += 1
            if changed > 1:
                return False
            if i == 0 or nums[i - 1] <= nums[i + 1]:
                nums[i] = nums[i + 1]
            else:
                nums[i + 1] = nums[i]
        return True
