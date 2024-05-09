
class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7

        def single(c):
            if c == '0': return 0
            if c == '*': return 9
            return 1

        def pair(a, b):
            if a == '*' and b == '*':
                return 15  # 11-19 (9) and 21-26 (6)
            if a == '*':
                if b <= '6':
                    return 2  # 1b or 2b
                else:
                    return 1  # only 1b
            if b == '*':
                if a == '1': return 9  # 11-19
                if a == '2': return 6  # 21-26
                return 0
            val = (ord(a) - 48) * 10 + (ord(b) - 48)
            return 1 if 10 <= val <= 26 else 0

        if not s: return 0

        prev = 1
        curr = single(s[0]) % MOD
        for i in range(1, len(s)):
            next_val = (curr * single(s[i]) + prev * pair(s[i-1], s[i])) % MOD
            prev, curr = curr, next_val
        return curr % MOD
