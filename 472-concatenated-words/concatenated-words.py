
from typing import List

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # Sort by length. For each word run word break using only shorter words seen so far.
        words.sort(key=len)
        shorter = set()
        result = []

        for w in words:
            if not w:
                continue

            n = len(w)
            dp = [False] * (n + 1)
            dp[0] = True

            # Standard word break. Check if w can be formed by words in shorter.
            for i in range(1, n + 1):
                for j in range(i):
                    if not dp[j]:
                        continue
                    if w[j:i] in shorter:
                        dp[i] = True
                        break

            if dp[n]:
                result.append(w)

            shorter.add(w)

        return result
