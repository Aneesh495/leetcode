
class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        last = {int(d): i for i, d in enumerate(s)}
        for i, ch in enumerate(s):
            curr = int(ch)
            for d in range(9, curr, -1):
                if d in last and last[d] > i:
                    j = last[d]
                    s[i], s[j] = s[j], s[i]
                    return int("".join(s))
        return num
