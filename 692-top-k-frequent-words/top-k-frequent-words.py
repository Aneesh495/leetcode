
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        return [w for w, _ in sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:k]]
