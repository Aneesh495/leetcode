
from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        # Backtrack building expressions that evaluate to target
        # Keep running total and last operand to handle multiplication precedence
        n = len(num)
        out: List[str] = []

        def dfs(i: int, expr: str, total: int, last: int) -> None:
            # If we used all digits then check if total hits target
            if i == n:
                if total == target:
                    out.append(expr)
                return

            # Try every split num[i:j+1] as the next operand
            for j in range(i, n):
                # Disallow numbers with leading zeros like "05"
                if j > i and num[i] == '0':
                    break
                s = num[i:j + 1]
                val = int(s)

                if i == 0:
                    # First number starts the expression
                    dfs(j + 1, s, val, val)
                else:
                    # Addition
                    dfs(j + 1, expr + '+' + s, total + val, val)
                    # Subtraction
                    dfs(j + 1, expr + '-' + s, total - val, -val)
                    # Multiplication
                    dfs(j + 1, expr + '*' + s, total - last + last * val, last * val)

        dfs(0, '', 0, 0)
        return out
