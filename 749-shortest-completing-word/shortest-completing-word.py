
from collections import Counter
from typing import List

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        need = Counter(ch.lower() for ch in licensePlate if ch.isalpha())
        best = None
        for w in words:
            cw = Counter(w.lower())
            if all(cw[c] >= need[c] for c in need):
                if best is None or len(w) < len(best):
                    best = w
        return best
