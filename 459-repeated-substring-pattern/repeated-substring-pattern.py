
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        Idea
        A string with a repeating unit will appear inside the middle of s plus s
        We remove the first and last characters to avoid the trivial full match
        Then we test membership
        Time O(n)
        Space O(1) extra besides the new string
        """
        return s in (s + s)[1:-1]
