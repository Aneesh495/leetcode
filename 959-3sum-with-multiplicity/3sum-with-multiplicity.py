
from collections import Counter

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10**9 + 7
        cnt = Counter(arr)
        keys = sorted(cnt)
        ans = 0
        for i, x in enumerate(keys):
            for j in range(i, len(keys)):
                y = keys[j]
                z = target - x - y
                if z < y:
                    continue
                if z not in cnt:
                    continue
                cx, cy, cz = cnt[x], cnt[y], cnt[z]
                if x == y == z:
                    if cx >= 3:
                        ans += cx * (cx - 1) * (cx - 2) // 6
                elif x == y != z:
                    if cx >= 2:
                        ans += (cx * (cx - 1) // 2) * cz
                elif x < y == z:
                    if cy >= 2:
                        ans += cx * (cy * (cy - 1) // 2)
                else:  # x < y < z
                    ans += cx * cy * cz
                ans %= MOD
        return ans % MOD
