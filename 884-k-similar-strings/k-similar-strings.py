
from collections import deque

class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        if s1 == s2:
            return 0
        q = deque([s1])
        seen = {s1}
        steps = 0
        n = len(s1)

        while q:
            for _ in range(len(q)):
                s = q.popleft()
                if s == s2:
                    return steps

                i = 0
                while i < n and s[i] == s2[i]:
                    i += 1
                if i == n:
                    continue

                best = []
                others = []
                for j in range(i + 1, n):
                    if s[j] == s2[i]:
                        if s[j] != s2[j]:
                            best.append(j)
                        else:
                            others.append(j)

                cand = best if best else others
                for j in cand:
                    ns = list(s)
                    ns[i], ns[j] = ns[j], ns[i]
                    ns = ''.join(ns)
                    if ns not in seen:
                        seen.add(ns)
                        q.append(ns)
            steps += 1
        return -1
