
class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def zeta(n: int) -> int:
            s = 0
            while n:
                n //= 5
                s += n
            return s

        def lower_bound(target: int) -> int:
            lo, hi = 0, 5 * (target + 1)
            while lo < hi:
                mid = (lo + hi) // 2
                if zeta(mid) < target:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        return 5 if lower_bound(k + 1) - lower_bound(k) == 5 else 0
