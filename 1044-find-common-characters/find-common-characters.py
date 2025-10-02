
from typing import List
from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Start with the frequency of characters in the first word
        common = Counter(words[0])

        # Intersect with each subsequent word's frequency
        # The '&=' keeps the minimum count for every character across words
        for w in words[1:]:
            common &= Counter(w)

        # Expand the multiset into the required list of characters
        # Each character appears as many times as its final count
        ans: List[str] = []
        for ch, cnt in common.items():
            ans.extend([ch] * cnt)

        return ans
