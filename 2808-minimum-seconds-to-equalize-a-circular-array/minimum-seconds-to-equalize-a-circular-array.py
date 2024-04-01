from collections import defaultdict
class Solution:
    def minimumSeconds(self, nums: list[int]) -> int:
        pos = defaultdict(list)
        n = len(nums)
        for i, x in enumerate(nums):
            pos[x].append(i)
        ans = n
        for idxs in pos.values():
            idxs.append(idxs[0] + n)
            mx = max(idxs[i + 1] - idxs[i] for i in range(len(idxs) - 1))
            ans = min(ans, mx // 2)
        return ans
