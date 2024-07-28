
from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if k <= 0 or total % k != 0:
            return False
        target = total // k
        nums.sort(reverse=True)
        if nums[0] > target:
            return False

        buckets = [0] * k
        n = len(nums)

        def dfs(idx: int) -> bool:
            if idx == n:
                return True
            v = nums[idx]
            seen = set()
            for i in range(k):
                if buckets[i] in seen:
                    continue
                if buckets[i] + v <= target:
                    seen.add(buckets[i])
                    buckets[i] += v
                    if dfs(idx + 1):
                        return True
                    buckets[i] -= v
                if buckets[i] == 0:
                    break
            return False

        return dfs(0)
