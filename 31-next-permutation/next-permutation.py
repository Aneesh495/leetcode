
from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Modifies nums in place to the next lexicographic permutation
        If no such permutation exists then rearranges to the lowest order
        """

        # Step 1 find the first index i from the right where nums[i] < nums[i + 1]
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # If i is found then there exists a higher permutation
        if i >= 0:
            # Step 2 find the smallest number greater than nums[i] to the right of i
            # Since the suffix is nonincreasing the first element from the right that is greater works
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Step 3 swap pivot nums[i] with nums[j]
            nums[i], nums[j] = nums[j], nums[i]

        # Step 4 reverse the suffix starting at i + 1 to make it the lowest order
        left = i + 1
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1