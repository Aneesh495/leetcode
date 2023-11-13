
from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # Modified merge sort that counts pairs where nums[i] > 2 * nums[j]
        def sort_count(lo: int, hi: int) -> int:
            if hi - lo <= 1:
                return 0

            mid = (lo + hi) // 2
            cnt = sort_count(lo, mid) + sort_count(mid, hi)

            # Count cross pairs where i in [lo, mid) and j in [mid, hi)
            j = mid
            for i in range(lo, mid):
                while j < hi and nums[i] > 2 * nums[j]:
                    j += 1
                cnt += j - mid

            # Merge step for standard merge sort
            temp = []
            i, j = lo, mid
            while i < mid and j < hi:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
            if i < mid:
                temp.extend(nums[i:mid])
            if j < hi:
                temp.extend(nums[j:hi])

            nums[lo:hi] = temp
            return cnt

        return sort_count(0, len(nums))
