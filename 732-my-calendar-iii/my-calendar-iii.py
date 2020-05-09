
from collections import defaultdict

class MyCalendarThree:
    def __init__(self):
        self.tree = defaultdict(int)
        self.lazy = defaultdict(int)

    def _update(self, ql, qr, l, r, idx):
        if ql > r or qr < l:
            return
        if ql <= l and r <= qr:
            self.tree[idx] += 1
            self.lazy[idx] += 1
            return
        mid = (l + r) // 2
        self._update(ql, qr, l, mid, idx * 2)
        self._update(ql, qr, mid + 1, r, idx * 2 + 1)
        self.tree[idx] = self.lazy[idx] + max(self.tree[idx * 2], self.tree[idx * 2 + 1])

    def book(self, startTime: int, endTime: int) -> int:
        self._update(startTime, endTime - 1, 0, 10**9, 1)
        return self.tree[1]
