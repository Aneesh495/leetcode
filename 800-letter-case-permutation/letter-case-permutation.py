
from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = ['']
        for ch in s:
            if ch.isalpha():
                res = [p + ch.lower() for p in res] + [p + ch.upper() for p in res]
            else:
                res = [p + ch for p in res]
        return res
