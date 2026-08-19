class Solution:
    def countValidSubstrings(self, s: str) -> int:
        forbidden_through = -1
        total = 0
        for right in range(len(s)):
            if right >= 2 and s[right - 2:right + 1] == 'abc':
                forbidden_through = right - 2
            # Only starts to the right of the most recent abc can be valid.
            total += right - forbidden_through
        return total