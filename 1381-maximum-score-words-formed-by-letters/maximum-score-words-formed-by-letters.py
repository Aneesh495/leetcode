from typing import List
from collections import Counter

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        available = Counter(letters)
        word_counts = [Counter(word) for word in words]
        word_scores = [
            sum(score[ord(c) - ord('a')] * cnt for c, cnt in wc.items())
            for wc in word_counts
        ]

        def dfs(i: int) -> int:
            if i == len(words):
                return 0

            best = dfs(i + 1)

            wc = word_counts[i]
            if all(available[c] >= wc[c] for c in wc):
                for c in wc:
                    available[c] -= wc[c]
                best = max(best, word_scores[i] + dfs(i + 1))
                for c in wc:
                    available[c] += wc[c]

            return best

        return dfs(0)
