
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Sort to enable two pointer scan and easy duplicate skipping
        nums.sort()
        n = len(nums)
        res: List[List[int]] = []

        for i in range(n - 3):
            # Skip duplicate a
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Prune by smallest and largest possible sums using current i
            min_sum = nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3]
            if min_sum > target:
                break
            max_sum = nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3]
            if max_sum < target:
                continue

            for j in range(i + 1, n - 2):
                # Skip duplicate b
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # Prune inside j layer
                min_sum_j = nums[i] + nums[j] + nums[j + 1] + nums[j + 2]
                if min_sum_j > target:
                    break
                max_sum_j = nums[i] + nums[j] + nums[n - 1] + nums[n - 2]
                if max_sum_j < target:
                    continue

                l = j + 1
                r = n - 1
                need = target - nums[i] - nums[j]

                while l < r:
                    s = nums[l] + nums[r]
                    if s == need:
                        res.append([nums[i], nums[j], nums[l], nums[r]])

                        # Move l to next different value
                        val_l = nums[l]
                        while l < r and nums[l] == val_l:
                            l += 1

                        # Move r to previous different value
                        val_r = nums[r]
                        while l < r and nums[r] == val_r:
                            r -= 1

                    elif s < need:
                        l += 1
                    else:
                        r -= 1

        return res