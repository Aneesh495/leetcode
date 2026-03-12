
from typing import List
from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # Helper to check if a string has valid parentheses
        def is_valid(t: str) -> bool:
            bal = 0
            for ch in t:
                if ch == '(':
                    bal += 1
                elif ch == ')':
                    if bal == 0:
                        return False
                    bal -= 1
            return bal == 0

        # BFS over strings formed by deleting one parenthesis at each step
        res = []
        visited = set([s])
        q = deque([s])
        found = False

        while q:
            cur = q.popleft()
            if is_valid(cur):
                res.append(cur)
                found = True
            if found:
                # Do not generate next level once any valid found at this level
                continue
            for i, ch in enumerate(cur):
                if ch not in ('(', ')'):
                    continue
                nxt = cur[:i] + cur[i+1:]
                if nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)

        return res if res else [""]
