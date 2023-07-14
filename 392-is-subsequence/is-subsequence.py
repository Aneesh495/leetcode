
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Two pointers
        Walk t once and advance pointer in s on matches
        s is a subsequence of t if we consume all chars in s
        Time O(len(t))  Space O(1)
        """
        i = 0  # pointer in s
        for ch in t:
            if i < len(s) and s[i] == ch:
                i += 1
                if i == len(s):  # all chars in s matched
                    return True
        return i == len(s)
