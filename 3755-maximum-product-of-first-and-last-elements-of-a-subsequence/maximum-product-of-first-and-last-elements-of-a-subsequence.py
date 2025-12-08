class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        n = len(nums)
        suffix_min = [0] * n
        suffix_max = [0] * n
        suffix_min[-1] = suffix_max[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])
            suffix_max[i] = max(nums[i], suffix_max[i + 1])
        answer = -10**30
        for i in range(n - m + 1):
            last_start = i + m - 1
            answer = max(answer, nums[i] * suffix_min[last_start], nums[i] * suffix_max[last_start])
        return answer