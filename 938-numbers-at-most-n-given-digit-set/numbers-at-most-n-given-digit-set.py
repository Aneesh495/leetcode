
from typing import List

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        s = str(n)
        k = len(s)
        m = len(digits)
        ans = 0

        # count numbers with length less than k
        for l in range(1, k):
            ans += m ** l

        # count numbers with the same length
        for i, ch in enumerate(s):
            smaller = sum(1 for d in digits if d < ch)
            ans += smaller * (m ** (k - i - 1))
            if ch not in digits:
                return ans
        return ans + 1
