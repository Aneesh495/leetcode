
from typing import List

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        arr.sort()
        index = {x: i for i, x in enumerate(arr)}
        dp = [1] * len(arr)  # single-node tree for each value

        for i, x in enumerate(arr):
            for j in range(i):
                a = arr[j]
                if x % a == 0:
                    b = x // a
                    if b in index:
                        dp[i] = (dp[i] + dp[j] * dp[index[b]]) % MOD

        return sum(dp) % MOD
