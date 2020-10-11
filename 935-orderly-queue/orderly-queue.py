
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            return "".join(sorted(s))
        best = s
        for i in range(1, len(s)):
            rotation = s[i:] + s[:i]
            if rotation < best:
                best = rotation
        return best
