
class Solution:
    def clumsy(self, n: int) -> int:
        # Use a stack to apply *, /, +, - in a repeating cycle on descending integers
        stack = [n]
        op = 0  # 0 mul, 1 div, 2 add, 3 sub
        for x in range(n - 1, 0, -1):
            if op == 0:
                stack[-1] = stack[-1] * x
            elif op == 1:
                # Division must truncate toward zero per problem statement
                stack[-1] = int(stack[-1] / x)
            elif op == 2:
                stack.append(x)
            else:
                stack.append(-x)
            op = (op + 1) % 4
        return sum(stack)
