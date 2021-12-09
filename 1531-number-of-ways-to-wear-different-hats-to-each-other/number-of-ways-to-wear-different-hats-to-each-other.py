class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        mod = 1_000_000_007
        people = [[] for _ in range(41)]
        for i, options in enumerate(hats):
            for h in options: people[h].append(i)
        dp = [0] * (1 << len(hats))
        dp[0] = 1
        for h in range(1, 41):
            nxt = dp[:]
            for mask, count in enumerate(dp):
                if count:
                    for person in people[h]:
                        if not mask & (1 << person):
                            new = mask | (1 << person)
                            nxt[new] = (nxt[new] + count) % mod
            dp = nxt
        return dp[-1]