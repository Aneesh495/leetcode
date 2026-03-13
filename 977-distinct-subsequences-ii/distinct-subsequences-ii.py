
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        end = [0] * 26
        total = 0
        for ch in s:
            i = ord(ch) - 97
            new = (total + 1 - end[i]) % MOD
            end[i] = (end[i] + new) % MOD
            total = (total + new) % MOD
        return total % MOD
