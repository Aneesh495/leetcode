
class Solution:
    def solveEquation(self, equation: str) -> str:
        def parse(expr: str):
            coef = const = 0
            i = 0
            sign = 1
            n = len(expr)
            while i < n:
                if expr[i] == '+':
                    sign = 1
                    i += 1
                elif expr[i] == '-':
                    sign = -1
                    i += 1
                else:
                    num = 0
                    has_num = False
                    while i < n and expr[i].isdigit():
                        num = num * 10 + int(expr[i])
                        i += 1
                        has_num = True
                    if i < n and expr[i] == 'x':
                        if not has_num:
                            num = 1
                        coef += sign * num
                        i += 1
                    else:
                        const += sign * num
            return coef, const

        left, right = equation.split('=')
        lc, lv = parse(left)
        rc, rv = parse(right)

        a = lc - rc           # coefficient of x on LHS after moving terms
        b = rv - lv           # constant on RHS after moving terms

        if a == 0:
            if b == 0:
                return "Infinite solutions"
            return "No solution"
        return f"x={b // a}"
