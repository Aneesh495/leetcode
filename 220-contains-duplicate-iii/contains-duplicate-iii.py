
from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        # If valueDiff is negative no pair can satisfy abs difference
        if valueDiff < 0 or indexDiff <= 0:
            return False

        w = valueDiff + 1  # Bucket width so any two in same bucket differ by <= valueDiff
        buckets = {}       # bucket_id -> value

        for i, x in enumerate(nums):
            bid = x // w  # Python floor division works for negatives too

            # Same bucket
            if bid in buckets:
                return True
            # Neighbor buckets can still be within valueDiff
            if bid - 1 in buckets and abs(x - buckets[bid - 1]) <= valueDiff:
                return True
            if bid + 1 in buckets and abs(x - buckets[bid + 1]) <= valueDiff:
                return True

            buckets[bid] = x

            # Maintain sliding window of size indexDiff
            if i >= indexDiff:
                old = nums[i - indexDiff]
                del buckets[old // w]

        return False
