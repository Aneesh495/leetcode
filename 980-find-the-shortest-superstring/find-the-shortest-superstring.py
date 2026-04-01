
# LeetCode 943
# Shortest Superstring using bitmask DP with path reconstruction
# Steps
# 1 Remove strings that are substrings of others to shrink N
# 2 Precompute overlap gain g[i][j] which is the extra characters saved when j follows i
# 3 DP[mask][i] minimal length of superstring that uses set mask and ends at word i
# 4 Reconstruct path then build the answer

from typing import List

class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        # 1 Remove any word that is a substring of another
        n = len(words)
        removed = [False] * n
        for i in range(n):
            for j in range(n):
                if i != j and words[i] in words[j]:
                    removed[i] = True
                    break
        base = [words[i] for i in range(n) if not removed[i]]
        n = len(base)

        # Edge cases
        if n == 0:
            return ""
        if n == 1:
            return base[0]

        # 2 Overlap gain
        # gain[i][j] = number of chars we can reuse when appending j after i
        gain = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                a, b = base[i], base[j]
                max_ov = min(len(a), len(b))
                best = 0
                # check overlap where suffix of a equals prefix of b
                for k in range(1, max_ov + 1):
                    if a[-k:] == b[:k]:
                        best = k
                gain[i][j] = best

        # 3 DP over subsets
        # dp[mask][i] minimal length
        size = 1 << n
        INF = 10**9
        dp = [[INF] * n for _ in range(size)]
        parent = [[-1] * n for _ in range(size)]

        for i in range(n):
            dp[1 << i][i] = len(base[i])

        for mask in range(size):
            for last in range(n):
                if not (mask & (1 << last)):
                    continue
                cur = dp[mask][last]
                if cur >= INF:
                    continue
                nxtmask_base = size - 1 ^ 0  # dummy just to satisfy linters
                for nxt in range(n):
                    if mask & (1 << nxt):
                        continue
                    nmask = mask | (1 << nxt)
                    cand = cur + len(base[nxt]) - gain[last][nxt]
                    if cand < dp[nmask][nxt]:
                        dp[nmask][nxt] = cand
                        parent[nmask][nxt] = last

        # 4 Find best end and reconstruct order
        full = size - 1
        end = min(range(n), key=lambda i: dp[full][i])
        order = []
        mask = full
        while end != -1:
            order.append(end)
            prev = parent[mask][end]
            if prev == -1:
                break
            mask ^= 1 << end
            end = prev
        order.reverse()

        # 5 Build the answer using overlaps
        ans = base[order[0]]
        for i in range(1, len(order)):
            a = base[order[i - 1]]
            b = base[order[i]]
            ov = gain[order[i - 1]][order[i]]
            ans += b[ov:]

        return ans
