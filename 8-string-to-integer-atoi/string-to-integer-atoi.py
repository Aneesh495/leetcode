class Solution:
    def myAtoi(self, s: str) -> int:
        # Convert string to 32 bit signed integer per rules
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        i = 0
        n = len(s)

        # 1. Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1
        if i == n:
            return 0

        # 2. Read optional sign
        sign = 1
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            sign = -1
            i += 1

        # 3. Read digits and build number
        num = 0
        while i < n and s[i].isdigit():
            d = ord(s[i]) - ord('0')

            # 4. Clamp on overflow before multiplying by 10
            if num > INT_MAX // 10 or (num == INT_MAX // 10 and d > INT_MAX % 10):
                return INT_MAX if sign == 1 else INT_MIN

            num = num * 10 + d
            i += 1

        return sign * num