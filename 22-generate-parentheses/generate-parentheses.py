
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Backtracking builds strings that never place a closing parenthesis
        # before its matching opening one. We add '(' if we still have some left
        # and add ')' only when it will not break validity.
        res: List[str] = []
        path: List[str] = []

        def dfs(open_left: int, close_left: int) -> None:
            # If no parentheses remain we found a valid combination
            if open_left == 0 and close_left == 0:
                res.append("".join(path))
                return

            # Place '(' if available
            if open_left > 0:
                path.append('(')
                dfs(open_left - 1, close_left)
                path.pop()

            # Place ')' only if it will not exceed the number of '(' used
            if close_left > open_left:
                path.append(')')
                dfs(open_left, close_left - 1)
                path.pop()

        dfs(n, n)
        return res