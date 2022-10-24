class Solution:
    def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
        # The target is guaranteed to exist, so the minimum is well-defined.
        return min(abs(i - start) for i, value in enumerate(nums) if value == target)