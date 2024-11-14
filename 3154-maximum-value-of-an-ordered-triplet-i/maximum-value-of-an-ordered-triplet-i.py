class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        suffix_max = [0] * n
        suffix_max[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(nums[i], suffix_max[i + 1])
        prefix_max = nums[0]
        best = 0
        for j in range(1, n - 1):
            best = max(best, (prefix_max - nums[j]) * suffix_max[j + 1])
            prefix_max = max(prefix_max, nums[j])
        return best