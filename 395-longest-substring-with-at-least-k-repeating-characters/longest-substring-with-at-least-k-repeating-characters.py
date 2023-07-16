
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        res = 0
        for target in range(1, 27):
            cnt = [0] * 26
            l = 0
            unique = 0
            at_least_k = 0
            for r in range(n):
                idx = ord(s[r]) - 97
                if cnt[idx] == 0:
                    unique += 1
                cnt[idx] += 1
                if cnt[idx] == k:
                    at_least_k += 1
                while unique > target:
                    li = ord(s[l]) - 97
                    if cnt[li] == k:
                        at_least_k -= 1
                    cnt[li] -= 1
                    if cnt[li] == 0:
                        unique -= 1
                    l += 1
                if unique == target and unique == at_least_k:
                    res = max(res, r - l + 1)
        return res
