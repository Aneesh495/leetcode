class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # If either is "0" the product is "0"
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        # Result can be at most m + n digits
        res = [0] * (m + n)

        # Multiply from least significant digits
        for i in range(m - 1, -1, -1):
            d1 = ord(num1[i]) - 48  # faster than int(num1[i])
            carry = 0
            for j in range(n - 1, -1, -1):
                d2 = ord(num2[j]) - 48
                # Position in result for ones and carry
                p = i + j + 1

                # Current sum at this position
                s = d1 * d2 + res[p] + carry

                res[p] = s % 10
                carry = s // 10

            # Any remaining carry goes to the next left slot
            res[i] += carry

        # Convert to string and remove leading zeros
        i = 0
        while i < len(res) and res[i] == 0:
            i += 1
        # Join digits into the final string
        return "".join(str(d) for d in res[i:]) or "0"