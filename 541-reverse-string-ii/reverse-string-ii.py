
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # Process the string in blocks of length 2k
        # For each block reverse the first k characters and keep the next k characters in order
        res = []
        n = len(s)
        for i in range(0, n, 2 * k):
            # First k of this block reversed
            first = s[i:i + k][::-1]
            # Next k of this block unchanged
            second = s[i + k:i + 2 * k]
            res.append(first + second)
        return "".join(res)
