
from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Map each character in the alien order to its rank
        rank = {ch: i for i, ch in enumerate(order)}

        # Compare each adjacent pair of words
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            # Walk characters until they differ or one word ends
            j = 0
            while j < len(w1) and j < len(w2) and w1[j] == w2[j]:
                j += 1

            # If we reached the end of one word
            if j == len(w1) or j == len(w2):
                # If w1 is longer than w2 then order is invalid
                if len(w1) > len(w2):
                    return False
                # Otherwise they are in correct order
                continue

            # Characters differ at position j
            if rank[w1[j]] > rank[w2[j]]:
                return False

        # All adjacent pairs are in nondecreasing order
        return True
