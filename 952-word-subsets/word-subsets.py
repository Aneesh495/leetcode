
from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        req = [0]*26
        for b in words2:
            cnt = [0]*26
            for ch in b:
                cnt[ord(ch)-97] += 1
            for i in range(26):
                if cnt[i] > req[i]:
                    req[i] = cnt[i]
        ans = []
        for a in words1:
            cnt = [0]*26
            for ch in a:
                cnt[ord(ch)-97] += 1
            ok = True
            for i in range(26):
                if cnt[i] < req[i]:
                    ok = False
                    break
            if ok:
                ans.append(a)
        return ans
