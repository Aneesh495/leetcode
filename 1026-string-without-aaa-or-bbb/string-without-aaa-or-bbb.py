
class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        res = []
        while a > 0 or b > 0:
            if len(res) >= 2 and res[-1] == res[-2] == 'a':
                res.append('b')
                b -= 1
                continue
            if len(res) >= 2 and res[-1] == res[-2] == 'b':
                res.append('a')
                a -= 1
                continue
            if a >= b and a > 0:
                res.append('a')
                a -= 1
            elif b > 0:
                res.append('b')
                b -= 1
        return ''.join(res)
