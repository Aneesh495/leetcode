from math import gcd

class Solution:
    def maxValidSplits(self, nums: list[int]) -> int:
        n = len(nums)
        best = 0
        for removed in range(-1, n):
            suffix = [0] * (n + 1)
            for i in range(n - 1, -1, -1):
                suffix[i] = suffix[i + 1] if i == removed else gcd(nums[i], suffix[i + 1])
            prefix = 0
            score = 0
            for i, value in enumerate(nums):
                if i == removed:
                    continue
                prefix = gcd(prefix, value)
                # The positive prefix GCD cannot match an empty suffix's GCD of zero.
                score += prefix == suffix[i + 1]
            best = max(best, score)
        return best