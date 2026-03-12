

from collections import deque

class MyStack:
    def __init__(self):
        # Use a single queue
        self.q = deque()

    def push(self, x: int) -> None:
        # Enqueue new element
        self.q.append(x)
        # Rotate the queue to move the new element to the front
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        # The front holds the stack top
        return self.q.popleft()

    def top(self) -> int:
        # Peek the front element
        return self.q[0]

    def empty(self) -> bool:
        return not self.q
