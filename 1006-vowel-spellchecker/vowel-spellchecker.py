
from typing import List

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        # Build three lookup structures
        # 1 exact words for perfect match
        exact = set(wordlist)

        # 2 first word by lowercase for case insensitive match
        lower_first = {}
        for w in wordlist:
            lw = w.lower()
            if lw not in lower_first:
                lower_first[lw] = w

        # 3 first word by devoweled lowercase for vowel error match
        def devowel(s: str) -> str:
            # Replace aeiou with *
            vowels = set("aeiou")
            return "".join("*" if ch in vowels else ch for ch in s)

        devo_first = {}
        for w in wordlist:
            key = devowel(w.lower())
            if key not in devo_first:
                devo_first[key] = w

        ans = []
        for q in queries:
            # Rule order exact then case then vowel
            if q in exact:
                ans.append(q)
                continue

            lq = q.lower()
            if lq in lower_first:
                ans.append(lower_first[lq])
                continue

            k = devowel(lq)
            ans.append(devo_first.get(k, ""))

        return ans
