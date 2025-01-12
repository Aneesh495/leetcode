
class Solution:
    from functools import lru_cache

    def racecar(self, target: int) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dp(t: int) -> int:
            if t == 0:
                return 0
            k = t.bit_length()  # smallest k with 2^k - 1 >= t
            if (1 << k) - 1 == t:
                return k
            # Option 1: overshoot then reverse
            ans = k + 1 + dp((1 << k) - 1 - t)
            # Option 2: stop before overshoot, reverse, go back m, reverse
            for m in range(k - 1):
                dist_forward = (1 << (k - 1)) - 1
                dist_back = (1 << m) - 1
                rem = t - dist_forward + dist_back
                ans = min(ans, (k - 1) + 1 + m + 1 + dp(rem))
            return ans

        return dp(target)
