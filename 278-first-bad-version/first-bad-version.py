
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # Binary search for the first index where isBadVersion becomes True
        left = 1
        right = n
        while left < right:
            mid = left + (right - left) // 2  # avoid potential overflow in other languages
            if isBadVersion(mid):
                # mid is bad so the first bad is in [left, mid]
                right = mid
            else:
                # mid is good so the first bad is after mid
                left = mid + 1
        # left equals right and points to the first bad version
        return left
