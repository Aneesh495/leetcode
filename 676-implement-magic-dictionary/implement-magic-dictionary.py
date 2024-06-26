
from typing import List
from collections import defaultdict

class MagicDictionary:
    def __init__(self):
        self.patterns = defaultdict(set)

    def buildDict(self, dictionary: List[str]) -> None:
        self.patterns.clear()
        for w in dictionary:
            for i in range(len(w)):
                p = w[:i] + '*' + w[i+1:]
                self.patterns[p].add(w)

    def search(self, searchWord: str) -> bool:
        for i in range(len(searchWord)):
            p = searchWord[:i] + '*' + searchWord[i+1:]
            words = self.patterns.get(p, set())
            if len(words) > 1:
                return True
            if len(words) == 1 and (searchWord not in words):
                return True
        return False
