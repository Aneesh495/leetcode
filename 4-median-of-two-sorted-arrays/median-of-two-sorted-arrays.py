from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Binary search on the smaller array. Ensures log of min length time.
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)
        total = m + n
        half = total // 2

        left = 0
        right = m

        while True:
            i = (left + right) // 2                # Cut in nums1. Count on left side of nums1.
            j = half - i                            # Cut in nums2. Count on left side of nums2.

            left1 = nums1[i - 1] if i > 0 else float("-inf")
            right1 = nums1[i] if i < m else float("inf")
            left2 = nums2[j - 1] if j > 0 else float("-inf")
            right2 = nums2[j] if j < n else float("inf")

            # Correct partition found when every left value is not greater than every right value.
            if left1 <= right2 and left2 <= right1:
                if total % 2:                        # Odd length. Median is the next right value.
                    return float(min(right1, right2))
                # Even length. Median is mean of the two middle values.
                return (max(left1, left2) + min(right1, right2)) / 2.0

            # Move cut left or right in nums1.
            if left1 > right2:
                right = i - 1
            else:
                left = i + 1