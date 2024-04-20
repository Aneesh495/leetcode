class Solution:
    def minimumOperations(self, num: str) -> int:
        n = len(num)
        ans = n - (1 if '0' in num else 0)
        for suf in ('00', '25', '50', '75'):
            j = num.rfind(suf[1])
            if j != -1:
                i = num.rfind(suf[0], 0, j)
                if i != -1:
                    ans = min(ans, n - i - 2)
        return ans
