
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if set(b) - set(a):
            return -1
        n = (len(b) + len(a) - 1) // len(a)
        s = a * n
        for k in range(3):
            if b in s:
                return n + k
            s += a
        return -1
