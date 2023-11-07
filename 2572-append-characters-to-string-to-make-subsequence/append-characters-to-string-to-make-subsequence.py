class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        matched = 0
        for char in s:
            if char == t[matched]:
                matched += 1
                if matched == len(t):
                    return 0
        # Only the unmatched suffix of t still needs to be appended.
        return len(t) - matched