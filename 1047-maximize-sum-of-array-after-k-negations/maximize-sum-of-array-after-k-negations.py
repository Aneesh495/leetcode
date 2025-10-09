
from typing import List

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        """
        Greedy approach
        1. Sort by absolute value in descending order so the smallest absolute value sits last
        2. Flip every negative while we still have flips to use
        3. If flips remain and k is odd then flip the element with the smallest absolute value
        4. Return the sum
        This is optimal because flipping a larger absolute value never helps after negatives are resolved
        Time O(n log n) due to sorting. Space O(1) extra
        """
        nums.sort(key=abs, reverse=True)

        for i in range(len(nums)):
            if k == 0:
                break
            if nums[i] < 0:
                nums[i] = -nums[i]
                k -= 1

        if k % 2 == 1:
            nums[-1] = -nums[-1]

        return sum(nums)
