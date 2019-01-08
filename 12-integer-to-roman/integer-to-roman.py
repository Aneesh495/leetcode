class Solution:
    def intToRoman(self, num: int) -> str:
        # Map values to symbols from high to low
        vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        # Build the answer greedily
        ans = []
        for v, s in zip(vals, syms):
            # Use symbol as many times as it fits
            k = num // v
            if k:
                ans.append(s * k)
                num -= v * k
            # Move to next value once current value no longer fits
        return "".join(ans)