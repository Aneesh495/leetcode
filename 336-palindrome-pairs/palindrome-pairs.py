
from typing import List

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # Map each word to its index for O(1) lookups
        index = {w: i for i, w in enumerate(words)}
        
        def is_pal(s: str) -> bool:
            # Two pointer palindrome check in O(len(s))
            i = 0
            j = len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        res_set = set()  # use a set to avoid duplicates

        for i, w in enumerate(words):
            L = len(w)
            # Try every split position including 0 and L
            # prefix = w[:j] suffix = w[j:]
            for j in range(L + 1):
                prefix = w[:j]
                suffix = w[j:]
                
                # Case 1
                # If prefix is palindrome then we can put reversed(suffix) in front
                # to form a palindrome
                if is_pal(prefix):
                    rev_suf = suffix[::-1]
                    if rev_suf in index and index[rev_suf] != i:
                        res_set.add((index[rev_suf], i))
                
                # Case 2
                # If suffix is palindrome then we can put reversed(prefix) at the end
                # to form a palindrome
                # Skip j == L to avoid duplicating Case 1 when suffix == ""
                if j != L and is_pal(suffix):
                    rev_pre = prefix[::-1]
                    if rev_pre in index and index[rev_pre] != i:
                        res_set.add((i, index[rev_pre]))
        
        # Convert set of tuples to the required list of lists
        return [list(p) for p in res_set]
