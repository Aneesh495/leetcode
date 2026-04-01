
from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # Simulate a stack. Push each value from pushed.
        # After each push keep popping while the top matches next in popped.
        stack = []
        j = 0
        for x in pushed:
            stack.append(x)
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        # Valid if we matched every element in popped.
        return j == len(popped)
