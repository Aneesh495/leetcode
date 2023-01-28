
class Solution:
    def calculate(self, s: str) -> int:
        # Single pass with a running result and sign
        # Use a stack to store outer result and sign when entering parentheses
        res = 0
        sign = 1
        num = 0
        stack = []

        for ch in s:
            if ch.isdigit():
                num = num * 10 + ord(ch) - 48
            elif ch == '+':
                res += sign * num
                num = 0
                sign = 1
            elif ch == '-':
                res += sign * num
                num = 0
                sign = -1
            elif ch == '(':
                # Push current context then reset for inner expression
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif ch == ')':
                # Close inner expression then apply stored sign and add to stored result
                res += sign * num
                num = 0
                res *= stack.pop()
                res += stack.pop()
            else:
                # Ignore spaces
                continue

        res += sign * num
        return res
