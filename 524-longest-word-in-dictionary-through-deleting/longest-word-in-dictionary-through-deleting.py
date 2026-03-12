
from typing import List

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        """
        Return the longest word in dictionary that can be formed by deleting some
        characters of the string s. If there are multiple answers with the same
        length return the lexicographically smallest one. If none return "".
        """

        # Sort dictionary words by:
        # 1 length descending so longer words come first
        # 2 lexicographical ascending so for the same length the smallest comes first
        dictionary.sort(key=lambda w: (-len(w), w))

        # Two pointer subsequence check
        def is_subsequence(word: str, text: str) -> bool:
            i = 0  # pointer in word
            for ch in text:
                if i < len(word) and word[i] == ch:
                    i += 1
                    if i == len(word):
                        return True
            return i == len(word)

        # Scan sorted dictionary. First match is the answer due to sort order
        for w in dictionary:
            if is_subsequence(w, s):
                return w
        return ""
