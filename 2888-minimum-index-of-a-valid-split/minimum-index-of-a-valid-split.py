class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        counts = {}
        for value in nums:
            counts[value] = counts.get(value, 0) + 1
        dominant = max(counts, key=counts.get)
        total = counts[dominant]
        left = 0
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == dominant:
                left += 1
            right = total - left
            if left * 2 > i + 1 and right * 2 > n - i - 1:
                return i
        return -1