
from typing import *

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Fast path for different lengths
        if len(s) != len(t):
            return False

        # Problem states lowercase English letters
        # Use fixed array for O(1) space and O(n) time
        counts = [0] * 26

        for ch in s:
            counts[ord(ch) - 97] += 1

        for ch in t:
            i = ord(ch) - 97
            counts[i] -= 1
            if counts[i] < 0:
                return False

        return True

        # For Unicode inputs use:
        # from collections import Counter
        # return Counter(s) == Counter(t)
