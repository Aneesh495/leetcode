from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Return all unique triplets [a, b, c] such that a + b + c == 0.
        Approach
          1 Sort the array to enable two pointer scanning and easy duplicate skipping
          2 Fix each number i as the first element then two pointer search on the right part
          3 Skip duplicates for i and while moving left and right pointers
        Time  O(n^2) since the outer loop is n and the inner two pointer scan is O(n)
        Space O(1) extra ignoring the output
        """
        nums.sort()
        n = len(nums)
        res: List[List[int]] = []

        for i in range(n):
            # Skip duplicate first elements to avoid repeated triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Since array is sorted if the current value is greater than 0
            # then all following values are also greater than 0 so no triplet can sum to 0
            if nums[i] > 0:
                break

            left = i + 1
            right = n - 1
            target = -nums[i]

            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    res.append([nums[i], nums[left], nums[right]])

                    # Move both pointers and skip duplicates for the second and third elements
                    left_val = nums[left]
                    right_val = nums[right]
                    left += 1
                    right -= 1
                    while left < right and nums[left] == left_val:
                        left += 1
                    while left < right and nums[right] == right_val:
                        right -= 1

                elif s < target:
                    left += 1
                else:
                    right -= 1

        return res