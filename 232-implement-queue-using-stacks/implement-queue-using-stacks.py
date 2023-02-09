
class MyQueue:
    def __init__(self):
        # in_stack holds newest elements
        # out_stack holds elements in queue order
        self._in = []
        self._out = []

    def _move(self) -> None:
        # Move all items from in_stack to out_stack when out_stack is empty
        if not self._out:
            while self._in:
                self._out.append(self._in.pop())

    def push(self, x: int) -> None:
        # Enqueue at back
        self._in.append(x)

    def pop(self) -> int:
        # Dequeue from front
        self._move()
        return self._out.pop()

    def peek(self) -> int:
        # Front element
        self._move()
        return self._out[-1]

    def empty(self) -> bool:
        # True when both stacks are empty
        return not self._in and not self._out
