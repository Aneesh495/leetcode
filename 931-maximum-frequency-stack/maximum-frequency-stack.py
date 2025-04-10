
from collections import defaultdict

class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)
        self.group = defaultdict(list)
        self.maxf = 0

    def push(self, val: int) -> None:
        f = self.freq[val] + 1
        self.freq[val] = f
        if f > self.maxf:
            self.maxf = f
        self.group[f].append(val)

    def pop(self) -> int:
        val = self.group[self.maxf].pop()
        self.freq[val] -= 1
        if not self.group[self.maxf]:
            self.maxf -= 1
        return val
