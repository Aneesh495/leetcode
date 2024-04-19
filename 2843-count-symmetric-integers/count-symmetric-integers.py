class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for x in range(low, high + 1):
            s = str(x)
            if len(s) % 2 == 0:
                m = len(s) // 2
                if sum(map(int, s[:m])) == sum(map(int, s[m:])):
                    ans += 1
        return ans
