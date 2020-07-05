
from collections import deque
from typing import List

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        buckets = [deque() for _ in range(26)]
        for w in words:
            buckets[ord(w[0]) - 97].append((w, 0))
        ans = 0
        for ch in s:
            idx = ord(ch) - 97
            q = buckets[idx]
            for _ in range(len(q)):
                w, i = q.popleft()
                i += 1
                if i == len(w):
                    ans += 1
                else:
                    buckets[ord(w[i]) - 97].append((w, i))
        return ans
