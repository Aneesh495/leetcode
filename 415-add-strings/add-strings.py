
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # Two pointers from right to left and a carry
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        out = []

        while i >= 0 or j >= 0 or carry:
            # Convert current chars to ints without int() by using ASCII
            d1 = ord(num1[i]) - 48 if i >= 0 else 0
            d2 = ord(num2[j]) - 48 if j >= 0 else 0

            s = d1 + d2 + carry
            out.append(chr((s % 10) + 48))  # push current digit as a char
            carry = s // 10

            i -= 1
            j -= 1

        # Reverse collected digits to form the final string
        return "".join(reversed(out))
