
from typing import List

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        built = set([""])
        best = ""
        for w in words:
            if w[:-1] in built:
                built.add(w)
                if len(w) > len(best):
                    best = w
        return best
