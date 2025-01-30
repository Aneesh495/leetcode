
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)
        prev = [-1] * 26
        prev2 = [-1] * 26
        res = 0
        for i, ch in enumerate(s):
            idx = ord(ch) - 65
            res += (prev[idx] - prev2[idx]) * (i - prev[idx])
            prev2[idx] = prev[idx]
            prev[idx] = i
        for k in range(26):
            res += (prev[k] - prev2[k]) * (n - prev[k])
        return res
