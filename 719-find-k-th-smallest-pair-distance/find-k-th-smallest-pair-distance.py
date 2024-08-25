
from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()

        def count_leq(x: int) -> int:
            cnt = 0
            left = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > x:
                    left += 1
                cnt += right - left
            return cnt

        lo, hi = 0, nums[-1] - nums[0]
        while lo < hi:
            mid = (lo + hi) // 2
            if count_leq(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo
