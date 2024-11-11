class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones = [i for i, ch in enumerate(s) if ch == '1']
        if len(ones) < k:
            return ""
        best = None
        for i in range(len(ones) - k + 1):
            candidate = s[ones[i]:ones[i + k - 1] + 1]
            if best is None or (len(candidate), candidate) < (len(best), best):
                best = candidate
        return best