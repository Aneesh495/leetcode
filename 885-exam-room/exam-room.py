
import heapq

class ExamRoom:
    def __init__(self, n: int):
        self.n = n
        self.heap = []  # max-heap by negative distance
        self.start = {}  # start -> (l, r)
        self.end = {}    # end -> (l, r)
        self._add_interval(-1, n)

    def _dist(self, l, r):
        if l == -1:
            return r
        if r == self.n:
            return self.n - 1 - l
        return (r - l) // 2

    def _add_interval(self, l, r):
        interval = (l, r)
        heapq.heappush(self.heap, (-self._dist(l, r), l, r))
        self.start[l] = interval
        self.end[r] = interval

    def _remove_interval(self, l, r):
        if l in self.start and self.start[l] == (l, r):
            del self.start[l]
        if r in self.end and self.end[r] == (l, r):
            del self.end[r]
        # lazy removal from heap

    def seat(self) -> int:
        while self.heap:
            _, l, r = heapq.heappop(self.heap)
            if self.start.get(l) == (l, r) and self.end.get(r) == (l, r):
                break
        # choose seat
        if l == -1:
            s = 0
        elif r == self.n:
            s = self.n - 1
        else:
            s = (l + r) // 2
        self._remove_interval(l, r)
        self._add_interval(l, s)
        self._add_interval(s, r)
        return s

    def leave(self, p: int) -> None:
        left = self.end.get(p)
        right = self.start.get(p)
        l = left[0]
        r = right[1]
        self._remove_interval(left[0], left[1])
        self._remove_interval(right[0], right[1])
        self._add_interval(l, r)
