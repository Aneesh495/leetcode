
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        for i in range(1, n - 1):
            if num[0] == '0' and i > 1:
                break
            a = num[:i]
            for j in range(i + 1, n):
                if num[i] == '0' and j - i > 1:
                    break
                b = num[i:j]
                k = j
                while k < n:
                    s = str(int(a) + int(b))
                    if not num.startswith(s, k):
                        break
                    k += len(s)
                    a, b = b, s
                if k == n:
                    return True
                a = num[:i]
        return False
