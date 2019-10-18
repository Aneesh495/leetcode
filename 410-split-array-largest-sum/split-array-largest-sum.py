
from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # Binary search on the answer
        # low is the minimum possible largest subarray sum which must be at least max(nums)
        # high is the maximum possible largest subarray sum which is sum(nums)
        low = max(nums)
        high = sum(nums)

        # Helper that returns how many subarrays are needed
        # if no subarray sum is allowed to exceed limit
        def required_splits(limit: int) -> int:
            parts = 1
            curr = 0
            for x in nums:
                if curr + x > limit:
                    parts += 1
                    curr = x
                else:
                    curr += x
            return parts

        while low < high:
            mid = (low + high) // 2
            if required_splits(mid) <= k:
                high = mid
            else:
                low = mid + 1
        return low
