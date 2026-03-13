
from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for num in range(left, right + 1):
            n = num
            ok = True
            while n:
                d = n % 10
                if d == 0 or num % d != 0:
                    ok = False
                    break
                n //= 10
            if ok:
                ans.append(num)
        return ans