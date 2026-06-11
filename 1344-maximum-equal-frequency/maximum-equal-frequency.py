from typing import List
from collections import Counter

class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        freq = Counter()
        freq_count = Counter()
        max_freq = 0
        ans = 0

        for i, x in enumerate(nums, 1):
            if freq[x]:
                freq_count[freq[x]] -= 1

            freq[x] += 1
            f = freq[x]
            freq_count[f] += 1
            max_freq = max(max_freq, f)

            if (
                max_freq == 1 or
                max_freq * freq_count[max_freq] + 1 == i or
                (max_freq - 1) * (freq_count[max_freq - 1] + 1) + 1 == i
            ):
                ans = i

        return ans
