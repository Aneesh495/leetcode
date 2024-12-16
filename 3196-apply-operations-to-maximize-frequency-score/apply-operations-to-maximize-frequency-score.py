from itertools import accumulate

class Solution:
    def maxFrequencyScore(self, nums: list[int], k: int) -> int:
        values = sorted(nums)
        sums = list(accumulate(values, initial=0))

        def cost(left: int, right: int) -> int:
            mid = (left + right) // 2
            median = values[mid]
            increase = median * (mid - left) - (sums[mid] - sums[left])
            decrease = sums[right + 1] - sums[mid + 1] - median * (right - mid)
            return increase + decrease

        # An optimal set can be chosen contiguous in sorted order and made equal to its median.
        left = 0
        best = 0
        for right in range(len(values)):
            while cost(left, right) > k:
                left += 1
            best = max(best, right - left + 1)
        return best