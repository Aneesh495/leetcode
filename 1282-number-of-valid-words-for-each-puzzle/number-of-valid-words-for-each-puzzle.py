from typing import List
from collections import Counter

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        def get_mask(s: str) -> int:
            mask = 0
            for ch in set(s):
                mask |= 1 << (ord(ch) - ord('a'))
            return mask

        freq = Counter()
        for word in words:
            mask = get_mask(word)
            if mask.bit_count() <= 7:
                freq[mask] += 1

        ans = []
        for puzzle in puzzles:
            first = 1 << (ord(puzzle[0]) - ord('a'))
            mask = 0
            for ch in puzzle[1:]:
                mask |= 1 << (ord(ch) - ord('a'))

            total = 0
            submask = mask
            while True:
                total += freq[submask | first]
                if submask == 0:
                    break
                submask = (submask - 1) & mask

            ans.append(total)

        return ans
