from typing import List

class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        MOD = 10**9 + 7

        def kadane(nums: List[int]) -> int:
            best = 0
            curr = 0
            for x in nums:
                curr = max(0, curr + x)
                best = max(best, curr)
            return best

        total = sum(arr)

        if k == 1:
            return kadane(arr) % MOD

        ans = kadane(arr * 2)
        if total > 0:
            ans += (k - 2) * total

        return ans % MOD
