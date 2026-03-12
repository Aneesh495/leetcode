
class Solution:
    def calculate(self, s: str) -> int:
        """
        Evaluate the expression with + - * / and spaces.
        Division must truncate toward zero.
        """
        stack = []
        num = 0
        sign = '+'

        for i, ch in enumerate(s + '+'):  # add a sentinel to flush the last number
            if ch.isdigit():
                num = num * 10 + ord(ch) - 48

            # when we hit an operator or the sentinel we resolve the previous sign
            if ch in '+-*/' or i == len(s):
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] = stack[-1] * num
                else:  # sign == '/'
                    # Python truncates toward zero when converting float to int
                    # Use int on true division to match the required behavior
                    prev = stack[-1]
                    stack[-1] = int(prev / num)

                sign = ch
                num = 0

        return sum(stack)
