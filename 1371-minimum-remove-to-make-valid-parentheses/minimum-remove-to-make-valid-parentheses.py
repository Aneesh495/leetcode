class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        chars = list(s)
        stack = []

        for i, ch in enumerate(chars):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                if stack:
                    stack.pop()
                else:
                    chars[i] = ''

        for i in stack:
            chars[i] = ''

        return ''.join(chars)
