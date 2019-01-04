class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Expand around a given center and return the bounds of the palindrome
        def expand(l: int, r: int) -> tuple[int, int]:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            # After the loop l and r are one step beyond the palindrome
            return l + 1, r - 1

        if not s:
            return ""

        start = 0
        end = 0

        for i in range(len(s)):
            # Odd length center at i
            l1, r1 = expand(i, i)
            # Even length center between i and i+1
            l2, r2 = expand(i, i + 1)

            # Pick the longer palindrome found at this index
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]