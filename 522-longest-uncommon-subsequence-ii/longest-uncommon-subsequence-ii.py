
from typing import List
from collections import Counter

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        # Return length of the longest string that is not a subsequence of any other
        def is_subseq(a: str, b: str) -> bool:
            # Check if a is a subsequence of b
            i = 0
            for ch in b:
                if i < len(a) and a[i] == ch:
                    i += 1
                if i == len(a):
                    return True
            return i == len(a)

        freq = Counter(strs)
        # Sort by length descending then lexicographically to stabilize order
        strs.sort(key=lambda s: (-len(s), s))

        checked = []  # strings already considered and are longer or equal in length
        for s in strs:
            if freq[s] > 1:
                # Duplicates cannot be uncommon
                checked.append(s)
                continue
            # If s is not a subsequence of any previously checked longer or equal strings then s is the answer
            if not any(is_subseq(s, t) for t in checked):
                return len(s)
            checked.append(s)

        return -1
