
from typing import List
from collections import defaultdict

class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        s = sum(nums)

        possible = any((s * k) % n == 0 for k in range(1, n))
        if not possible:
            return False

        trans = [x * n - s for x in nums]
        m = n // 2
        L, R = trans[:m], trans[m:]

        def subset_sums(arr):
            m = len(arr)
            sums_by_size = [set() for _ in range(m + 1)]
            sums_by_size[0].add(0)
            for mask in range(1, 1 << m):
                sm = 0
                b = 0
                i = 0
                tmp = mask
                while tmp:
                    if tmp & 1:
                        sm += arr[i]
                        b += 1
                    i += 1
                    tmp >>= 1
                sums_by_size[b].add(sm)
            return sums_by_size

        left = subset_sums(L)
        right = subset_sums(R)

        for k in range(1, len(left)):
            if 0 in left[k]:
                return True
        for k in range(1, len(right)):
            if 0 in right[k]:
                return True

        sum_to_sizes = defaultdict(set)
        for sz in range(len(right)):
            for v in right[sz]:
                sum_to_sizes[v].add(sz)

        for sl in range(len(left)):
            for v in left[sl]:
                need = -v
                if need in sum_to_sizes:
                    for sr in sum_to_sizes[need]:
                        tot = sl + sr
                        if 1 <= tot <= n - 1:
                            return True
        return False
