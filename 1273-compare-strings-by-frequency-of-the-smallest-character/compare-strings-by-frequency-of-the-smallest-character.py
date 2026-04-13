from typing import List
import bisect

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s: str) -> int:
            smallest = min(s)
            return s.count(smallest)

        word_freqs = sorted(f(w) for w in words)
        n = len(word_freqs)

        ans = []
        for q in queries:
            fq = f(q)
            idx = bisect.bisect_right(word_freqs, fq)
            ans.append(n - idx)

        return ans
