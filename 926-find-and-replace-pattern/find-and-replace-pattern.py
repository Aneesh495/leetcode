
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def canon(s: str):
            m = {}
            seq = []
            nxt = 0
            for ch in s:
                if ch not in m:
                    m[ch] = nxt
                    nxt += 1
                seq.append(m[ch])
            return tuple(seq)
        
        p = canon(pattern)
        return [w for w in words if canon(w) == p]
