from bisect import bisect_left, bisect_right

class Solution:
    def kthSmallestProduct(self, nums1: list[int], nums2: list[int], k: int) -> int:
        def count_at_most(x: int) -> int:
            total = 0
            for a in nums1:
                if a > 0:
                    total += bisect_right(nums2, x // a)
                elif a < 0:
                    threshold = -((-x) // a)
                    total += len(nums2) - bisect_left(nums2, threshold)
                elif x >= 0:
                    total += len(nums2)
            return total

        low, high = -10**10, 10**10
        while low < high:
            mid = (low + high) // 2
            if count_at_most(mid) >= k:
                high = mid
            else:
                low = mid + 1
        return low