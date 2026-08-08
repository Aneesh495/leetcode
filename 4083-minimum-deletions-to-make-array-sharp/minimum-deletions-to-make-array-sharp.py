class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        # Adjacent values XOR to zero exactly when they match. Keep one of each run.
        return sum(nums[i] == nums[i - 1] for i in range(1, len(nums)))