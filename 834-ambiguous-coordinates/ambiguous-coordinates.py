
from typing import List

class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def forms(t: str) -> List[str]:
            n = len(t)
            res = []
            if n == 1:
                return [t]
            if t[0] == '0' and t[-1] == '0':
                return res
            if t[0] == '0':
                return ["0." + t[1:]]
            if t[-1] == '0':
                return [t]
            res.append(t)
            for i in range(1, n):
                res.append(t[:i] + "." + t[i:])
            return res

        digits = s[1:-1]
        ans = []
        for i in range(1, len(digits)):
            left = digits[:i]
            right = digits[i:]
            for a in forms(left):
                for b in forms(right):
                    ans.append(f"({a}, {b})")
        return ans
