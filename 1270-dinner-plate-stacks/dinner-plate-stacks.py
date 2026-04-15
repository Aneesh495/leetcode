import heapq


class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []
        self.available = []  # min-heap of indices with space

    def _clean_available(self):
        while self.available:
            idx = self.available[0]
            if idx >= len(self.stacks) or len(self.stacks[idx]) == self.capacity:
                heapq.heappop(self.available)
            else:
                break

    def _clean_right(self):
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()

    def push(self, val: int) -> None:
        self._clean_available()

        if self.available:
            idx = heapq.heappop(self.available)
            self.stacks[idx].append(val)
            if len(self.stacks[idx]) < self.capacity:
                heapq.heappush(self.available, idx)
        else:
            if not self.stacks or len(self.stacks[-1]) == self.capacity:
                self.stacks.append([])
            self.stacks[-1].append(val)
            if len(self.stacks[-1]) < self.capacity:
                heapq.heappush(self.available, len(self.stacks) - 1)

    def pop(self) -> int:
        self._clean_right()
        if not self.stacks:
            return -1

        idx = len(self.stacks) - 1
        val = self.stacks[idx].pop()
        heapq.heappush(self.available, idx)

        self._clean_right()
        return val

    def popAtStack(self, index: int) -> int:
        if index < 0 or index >= len(self.stacks) or not self.stacks[index]:
            return -1

        val = self.stacks[index].pop()
        heapq.heappush(self.available, index)

        if index == len(self.stacks) - 1:
            self._clean_right()

        return val


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)
