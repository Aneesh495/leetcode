
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        res = []
        cnt = 0
        for ch in reversed(s):
            if ch == '-':
                continue
            if cnt == k:
                res.append('-')
                cnt = 0
            res.append(ch.upper())
            cnt += 1
        return ''.join(reversed(res))
