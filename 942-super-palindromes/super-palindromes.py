
class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        L, R = int(left), int(right)

        def is_pal(x: int) -> bool:
            s = str(x)
            return s == s[::-1]

        ans = 0
        LIMIT = 100000

        # odd-length palindromic roots
        for k in range(1, LIMIT):
            s = str(k)
            t = int(s + s[-2::-1])
            v = t * t
            if v > R:
                if k == 1 or (int(str(k + 1) + str(k + 1)[-2::-1]) ** 2 > v):
                    break
            if v >= L and is_pal(v):
                ans += 1

        # even-length palindromic roots
        for k in range(1, LIMIT):
            s = str(k)
            t = int(s + s[::-1])
            v = t * t
            if v > R:
                if k == 1 or (int(str(k + 1) + str(k + 1)[::-1]) ** 2 > v):
                    break
            if v >= L and is_pal(v):
                ans += 1

        return ans
