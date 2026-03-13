
from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        wlen = n - k + 1
        w = [0] * wlen
        curr = sum(nums[:k])
        w[0] = curr
        for i in range(1, wlen):
            curr += nums[i + k - 1] - nums[i - 1]
            w[i] = curr

        left = [0] * wlen
        best = 0
        for i in range(wlen):
            if w[i] > w[best]:
                best = i
            left[i] = best

        right = [0] * wlen
        best = wlen - 1
        for i in range(wlen - 1, -1, -1):
            if w[i] >= w[best]:
                best = i
            right[i] = best

        ans = [-1, -1, -1]
        best_total = -1
        for m in range(k, wlen - k):
            l = left[m - k]
            r = right[m + k]
            total = w[l] + w[m] + w[r]
            if total > best_total:
                best_total = total
                ans = [l, m, r]
        return ans
