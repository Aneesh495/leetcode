
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # KMP search
        # Edge case
        if not needle:
            return 0

        # Build LPS array where lps[i] is the length of the longest
        # proper prefix of needle[:i+1] that is also a suffix
        lps = [0] * len(needle)
        length = 0
        i = 1
        while i < len(needle):
            if needle[i] == needle[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        # Scan haystack using the LPS table
        i = 0  # index for haystack
        j = 0  # index for needle
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == len(needle):
                    return i - j
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return -1
