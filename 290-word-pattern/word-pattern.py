
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        p2w, w2p = {}, {}
        for ch, w in zip(pattern, words):
            if ch in p2w:
                if p2w[ch] != w:
                    return False
            else:
                if w in w2p:
                    return False
                p2w[ch] = w
                w2p[w] = ch
        return True
