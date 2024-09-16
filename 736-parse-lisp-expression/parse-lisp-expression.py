
class Solution:
    def evaluate(self, expression: str) -> int:
        scope = {}

        def get_val(token: str) -> int:
            if token[0] == '-' or token[0].isdigit():
                return int(token)
            # lookup from innermost scope outward
            if token in scope and scope[token]:
                return scope[token][-1]
            return 0

        def split_top(s: str):
            res, buf, bal = [], [], 0
            i = 0
            while i < len(s):
                c = s[i]
                if c == ' ' and bal == 0:
                    if buf:
                        res.append(''.join(buf))
                        buf = []
                else:
                    if c == '(':
                        bal += 1
                    elif c == ')':
                        bal -= 1
                    buf.append(c)
                i += 1
            if buf:
                res.append(''.join(buf))
            return res

        def eval_exp(exp: str) -> int:
            if exp[0] != '(':
                return get_val(exp)
            exp = exp[1:-1]
            tokens = split_top(exp)
            op = tokens[0]
            if op == 'add':
                return eval_exp(tokens[1]) + eval_exp(tokens[2])
            if op == 'mult':
                return eval_exp(tokens[1]) * eval_exp(tokens[2])
            # let
            # push new scope frame for any variables we see
            created = []
            i = 1
            while i < len(tokens) - 1:
                var = tokens[i]
                val = eval_exp(tokens[i + 1])
                if var not in scope:
                    scope[var] = []
                scope[var].append(val)
                created.append(var)
                i += 2
            res = eval_exp(tokens[-1])
            for v in created:
                scope[v].pop()
            return res

        return eval_exp(expression)
