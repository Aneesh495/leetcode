
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        # parse "a+bi" into integers a and b
        def parse(s: str):
            p = s.find('+')
            a = int(s[:p])
            b = int(s[p+1:-1])  # drop trailing 'i'
            return a, b

        a, b = parse(num1)
        c, d = parse(num2)

        real = a * c - b * d
        imag = a * d + b * c
        return f"{real}+{imag}i"
