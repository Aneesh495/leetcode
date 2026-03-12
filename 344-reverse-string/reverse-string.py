
from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        # Two pointers move toward center
        i = 0
        j = len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]  # swap in place
            i += 1
            j -= 1
