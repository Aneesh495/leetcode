
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        left_max = nums[0]
        max_so_far = nums[0]
        idx = 0
        for i in range(1, len(nums)):
            max_so_far = max(max_so_far, nums[i])
            if nums[i] < left_max:
                idx = i
                left_max = max_so_far
        return idx + 1
