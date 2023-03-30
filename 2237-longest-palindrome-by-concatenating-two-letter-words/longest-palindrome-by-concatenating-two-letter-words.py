from typing import List
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        counts = {}
        for word in words:
            counts[word] = counts.get(word, 0) + 1
        length = 0
        has_center = False

        for word, count in counts.items():
            reverse = word[::-1]
            if word < reverse:
                matching_pairs = min(count, counts.get(reverse, 0))
                length += matching_pairs * 4
            elif word == reverse:
                length += (count // 2) * 4
                if count % 2 == 1:
                    has_center = True
        if has_center:
            length += 2
        return length