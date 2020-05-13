
class WordFilter:
    def __init__(self, words: List[str]):
        self.d = {}
        for i, w in enumerate(words):
            L = len(w)
            for p in range(L + 1):
                pre = w[:p]
                for s in range(L + 1):
                    suf = w[L - s:]
                    self.d[(pre, suf)] = i

    def f(self, pref: str, suff: str) -> int:
        return self.d.get((pref, suff), -1)
