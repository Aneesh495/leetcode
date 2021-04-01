class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        i = 0
        def parse():
            nonlocal i
            union, product = set(), {''}
            while i < len(expression) and expression[i] != '}':
                c = expression[i]
                if c == ',':
                    union |= product
                    product = {''}
                    i += 1
                else:
                    if c == '{':
                        i += 1
                        part = parse()
                        i += 1
                    else:
                        part = {c}
                        i += 1
                    product = {a + b for a in product for b in part}
            return union | product
        return sorted(parse())