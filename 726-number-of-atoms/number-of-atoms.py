
from collections import Counter

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        i, n = 0, len(formula)
        stack = [Counter()]

        def parse_name():
            nonlocal i
            start = i
            i += 1  # first char is uppercase
            while i < n and formula[i].islower():
                i += 1
            return formula[start:i]

        def parse_num():
            nonlocal i
            if i >= n or not formula[i].isdigit():
                return 1
            start = i
            while i < n and formula[i].isdigit():
                i += 1
            return int(formula[start:i])

        while i < n:
            ch = formula[i]
            if ch == '(':
                i += 1
                stack.append(Counter())
            elif ch == ')':
                i += 1
                mult = parse_num()
                top = stack.pop()
                for k, v in top.items():
                    stack[-1][k] += v * mult
            elif ch.isupper():
                name = parse_name()
                num = parse_num()
                stack[-1][name] += num
            else:
                i += 1  # safety, though input should be valid

        result = []
        for elem in sorted(stack[-1].keys()):
            cnt = stack[-1][elem]
            result.append(elem)
            if cnt > 1:
                result.append(str(cnt))
        return "".join(result)
