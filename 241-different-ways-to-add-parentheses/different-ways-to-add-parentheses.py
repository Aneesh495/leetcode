
from typing import List, Dict, Tuple

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # Use memo to cache results for substrings
        memo: Dict[Tuple[int, int], List[int]] = {}
        s = expression
        n = len(s)

        def compute(op: str, a: int, b: int) -> int:
            if op == '+':
                return a + b
            if op == '-':
                return a - b
            return a * b  # op == '*'

        def dfs(l: int, r: int) -> List[int]:
            # Return all results for s[l:r]
            key = (l, r)
            if key in memo:
                return memo[key]

            # Check if the substring is a pure number
            is_num = True
            for i in range(l, r):
                c = s[i]
                if c == '+' or c == '-' or c == '*':
                    is_num = False
                    break
            if is_num:
                memo[key] = [int(s[l:r])]
                return memo[key]

            res: List[int] = []
            # Split around each operator
            for i in range(l, r):
                c = s[i]
                if c == '+' or c == '-' or c == '*':
                    left_vals = dfs(l, i)
                    right_vals = dfs(i + 1, r)
                    for a in left_vals:
                        for b in right_vals:
                            res.append(compute(c, a, b))

            memo[key] = res
            return res

        return dfs(0, n)
