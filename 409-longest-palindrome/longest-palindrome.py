
class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        freq = Counter(s)
        length = 0
        has_odd = 0
        for v in freq.values():
            length += (v // 2) * 2
            if v % 2:
                has_odd = 1
        return length + has_odd
