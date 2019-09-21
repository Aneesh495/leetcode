
import random
from collections import defaultdict

class RandomizedCollection:

    def __init__(self):
        self.arr = []
        self.pos = defaultdict(set)

    def insert(self, val: int) -> bool:
        exists = len(self.pos[val]) > 0
        self.pos[val].add(len(self.arr))
        self.arr.append(val)
        return not exists

    def remove(self, val: int) -> bool:
        if not self.pos[val]:
            return False
        i = self.pos[val].pop()
        last = self.arr[-1]
        last_i = len(self.arr) - 1
        if i != last_i:
            self.arr[i] = last
            self.pos[last].add(i)
            self.pos[last].discard(last_i)
        self.arr.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)
