from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Sort to enable two pointer sweep
        nums.sort()
        n = len(nums)

        # Initialize with any valid triple sum
        best = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            # Optional early skip of identical anchors to cut work
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = n - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]

                # Update best if this sum is closer
                if abs(s - target) < abs(best - target):
                    best = s

                # Exact hit found
                if s == target:
                    return target

                # Move pointers to approach target
                if s < target:
                    l += 1
                    # Optional skip of duplicates on left
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                else:
                    r -= 1
                    # Optional skip of duplicates on right
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return best

# Time O(n^2)
# Space O(1) extra aside from sorting in place