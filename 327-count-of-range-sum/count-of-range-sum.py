
from typing import List

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        # Prefix sums p where p[i] = sum(nums[:i])
        p = [0]
        s = 0
        for x in nums:
            s += x
            p.append(s)

        def sort_and_count(lo: int, hi: int) -> int:
            if hi - lo <= 1:
                return 0

            mid = (lo + hi) // 2
            cnt = sort_and_count(lo, mid) + sort_and_count(mid, hi)

            # Count valid pairs with two pointers
            l = r = mid
            for i in range(lo, mid):
                while l < hi and p[l] - p[i] < lower:
                    l += 1
                while r < hi and p[r] - p[i] <= upper:
                    r += 1
                cnt += r - l

            # Merge p[lo:mid] and p[mid:hi] in place
            tmp = []
            i, j = lo, mid
            while i < mid and j < hi:
                if p[i] <= p[j]:
                    tmp.append(p[i])
                    i += 1
                else:
                    tmp.append(p[j])
                    j += 1
            if i < mid:
                tmp.extend(p[i:mid])
            if j < hi:
                tmp.extend(p[j:hi])
            p[lo:hi] = tmp
            return cnt

        return sort_and_count(0, len(p))
