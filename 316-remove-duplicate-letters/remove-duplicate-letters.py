
from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        remaining = Counter(s)
        stack = []
        in_stack = set()

        for ch in s:
            remaining[ch] -= 1
            if ch in in_stack:
                continue
            while stack and ch < stack[-1] and remaining[stack[-1]] > 0:
                in_stack.remove(stack.pop())
            stack.append(ch)
            in_stack.add(ch)
        return "".join(stack)
