
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        L = len(n)
        num = int(n)

        def make_pal(s):
            left = s[:(L // 2)]
            mid = s[L // 2] if L % 2 else ''
            if L % 2:
                return s[:(L // 2 + 1)] + s[:L // 2][::-1]
            else:
                return s[:(L // 2)] + s[:L // 2][::-1]

        # Candidates from boundaries
        candidates = set()
        candidates.add(str(10 ** (L - 1) - 1))        # e.g., 999
        candidates.add(str(10 ** L + 1))              # e.g., 1001

        prefix = int(n[: (L + 1) // 2])
        for p in (prefix - 1, prefix, prefix + 1):
            s = str(p)
            if len(s) < (L + 1) // 2:
                s = '0' * (((L + 1) // 2) - len(s)) + s
            cand = s + (s[:-1] if L % 2 else s)[::-1]
            # Adjust to length L if overflowed or underflowed
            if len(cand) < L:
                cand = '9' * L
            elif len(cand) > L:
                cand = '1' + ('0' * (L - 1)) + '1'
            candidates.add(cand)

        candidates.discard(n)

        best = None
        for c in candidates:
            if c.lstrip('0') == '':
                val = 0
            else:
                val = int(c)
            diff = abs(val - num)
            if best is None:
                best = (diff, val)
            else:
                if diff < best[0] or (diff == best[0] and val < best[1]):
                    best = (diff, val)
        return str(best[1])
