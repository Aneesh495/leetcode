
from functools import lru_cache
from collections import defaultdict
from typing import List

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        trans = defaultdict(list)
        for trip in allowed:
            trans[trip[:2]].append(trip[2])

        @lru_cache(None)
        def can_build(level: str) -> bool:
            if len(level) == 1:
                return True

            # generate all possible next levels
            choices = []
            for i in range(len(level) - 1):
                pair = level[i:i+2]
                if pair not in trans:
                    return False
                choices.append(trans[pair])

            def backtrack(i: int, nxt: List[str]) -> bool:
                if i == len(choices):
                    return can_build(''.join(nxt))
                for ch in choices[i]:
                    nxt.append(ch)
                    if backtrack(i + 1, nxt):
                        return True
                    nxt.pop()
                return False

            return backtrack(0, [])

        return can_build(bottom)
