
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        """
        Longest Uncommon Subsequence I
        If both strings are equal then every subsequence is shared so return -1
        Otherwise the longer string itself is an uncommon subsequence so return its length
        """
        if a == b:
            return -1
        return max(len(a), len(b))
