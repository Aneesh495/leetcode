
class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.A = encoding
        self.i = 0

    def next(self, n: int) -> int:
        while self.i < len(self.A) and n > self.A[self.i]:
            n -= self.A[self.i]
            self.i += 2
        if self.i >= len(self.A):
            return -1
        self.A[self.i] -= n
        val = self.A[self.i + 1]
        if self.A[self.i] == 0:
            self.i += 2
        return val
