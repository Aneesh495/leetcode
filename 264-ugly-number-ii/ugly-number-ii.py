
from typing import List

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # dp[i] stores the i-th ugly number in one based sense
        dp: List[int] = [0] * n
        dp[0] = 1

        # pointers for the next multiples of 2 and 3 and 5
        i2 = i3 = i5 = 0

        # next candidate values from each prime
        next2 = 2
        next3 = 3
        next5 = 5

        for k in range(1, n):
            # choose the smallest next candidate
            nxt = min(next2, next3, next5)
            dp[k] = nxt

            # advance any pointer that produced the chosen value
            if nxt == next2:
                i2 += 1
                next2 = dp[i2] * 2
            if nxt == next3:
                i3 += 1
                next3 = dp[i3] * 3
            if nxt == next5:
                i5 += 1
                next5 = dp[i5] * 5

        return dp[-1]
