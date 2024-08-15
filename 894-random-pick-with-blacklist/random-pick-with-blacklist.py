
import random
from typing import List

class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        self.m = n - len(blacklist)
        black = set(blacklist)
        tail = iter(x for x in range(self.m, n) if x not in black)
        self.map = {}
        for b in blacklist:
            if b < self.m:
                w = next(tail)
                self.map[b] = w

    def pick(self) -> int:
        x = random.randint(0, self.m - 1)
        return self.map.get(x, x)
