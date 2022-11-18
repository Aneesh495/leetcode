class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        m = len(part)
        for char in s:
            stack.append(char)
            if len(stack) >= m and ''.join(stack[-m:]) == part:
                del stack[-m:]
        return ''.join(stack)