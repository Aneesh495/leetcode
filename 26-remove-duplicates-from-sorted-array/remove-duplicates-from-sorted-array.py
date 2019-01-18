
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Empty array case
        if not nums:
            return 0

        # write points to the next spot for a new unique value
        write = 1

        # read scans the array once
        for read in range(1, len(nums)):
            # When a new value appears copy it forward
            if nums[read] != nums[write - 1]:
                nums[write] = nums[read]
                write += 1

        # write is the count of unique values
        return write