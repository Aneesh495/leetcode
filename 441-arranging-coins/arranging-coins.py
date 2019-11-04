
class Solution:
    def arrangeCoins(self, n: int) -> int:
        # We need the largest k such that k*(k + 1)/2 <= n
        # Use binary search to avoid float precision issues
        lo, hi = 0, n
        while lo <= hi:
            mid = (lo + hi) // 2
            coins = mid * (mid + 1) // 2
            if coins == n:
                return mid
            if coins < n:
                lo = mid + 1
            else:
                hi = mid - 1
        # hi is the largest k with k*(k+1)/2 <= n
        return hi
