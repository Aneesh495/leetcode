class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        pair = {}
        stack = []

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                j = stack.pop()
                pair[i] = j
                pair[j] = i

        res = []
        i, step = 0, 1

        while 0 <= i < n:
            if s[i] == '(' or s[i] == ')':
                i = pair[i]
                step = -step
            else:
                res.append(s[i])
            i += step

        return ''.join(res)
