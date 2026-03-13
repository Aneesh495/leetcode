
from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        cnt = Counter(s)
        out = []
        for ch in order:
            if ch in cnt:
                out.append(ch * cnt.pop(ch))
        for ch, n in cnt.items():
            out.append(ch * n)
        return "".join(out)
