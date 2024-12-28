
class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def rle(t: str):
            chars, counts = [], []
            i, n = 0, len(t)
            while i < n:
                j = i
                while j < n and t[j] == t[i]:
                    j += 1
                chars.append(t[i])
                counts.append(j - i)
                i = j
            return chars, counts

        s_chars, s_counts = rle(s)
        ans = 0
        for w in words:
            w_chars, w_counts = rle(w)
            if w_chars != s_chars:
                continue
            ok = True
            for sc, wc in zip(s_counts, w_counts):
                if sc < wc:
                    ok = False
                    break
                if sc != wc and sc < 3:
                    ok = False
                    break
            if ok:
                ans += 1
        return ans
