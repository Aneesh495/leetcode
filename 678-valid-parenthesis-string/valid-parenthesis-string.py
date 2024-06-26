
class Solution:
    def checkValidString(self, s: str) -> bool:
        lo = hi = 0
        for ch in s:
            if ch == '(':
                lo += 1
                hi += 1
            elif ch == ')':
                lo = max(lo - 1, 0)
                hi -= 1
            else:  # '*'
                lo = max(lo - 1, 0)
                hi += 1
            if hi < 0:
                return False
        return lo == 0
